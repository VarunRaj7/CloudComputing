from flask import Flask,request,render_template
from flask_restful import reqparse, abort, Api, Resource

import urllib,json
import csv
import datetime
import operator
import numpy as np
import csv

app = Flask(__name__)
api = Api(app)

#Reading from the csv file code
filename="daily.csv"

rows=[]
with open(filename,'r') as csvfile:
    csvreader=csv.reader(csvfile)
    csvreader.next()
    for row in csvreader:
       rows.append(row)
y=csvreader.line_num
csvfile.close()
res1=[]
res2=[]

for i in range(0,y-1):
   res1.append({"DATE":rows[i][0]})
   res2.append({"DATE":rows[i][0],"TMAX":float(rows[i][1]),"TMIN":float(rows[i][2])})

ytmax=[]
ytmin=[]

for i in range(1463,1827):
   ytmax.append(rows[i][1])
   ytmin.append(rows[i][2])
#Reading ends here
   
#Linear regression of order 5
coef1=np.array([ 3.95974732e+01, 2.36990241e-01, -6.44656280e-04,  2.00737802e-05, -1.10753920e-07,  1.52765801e-10])
coef2=np.array([ 2.48085046e+01,  2.65541886e-01, -4.05219747e-03,  5.34037823e-05, -2.28988515e-07,  2.95562304e-10])
yntmax=[]

for i in range(1,367):
    x=np.array([1,i,i**2,i**3,i**4,i**5])
	yntmax.append((coef1*x).sum())

yntmin=[]
for i in range(1,365):
    x=np.array([1,i,i**2,i**3,i**4,i**5])
	yntmin.append((coef2*x).sum())
#Regression Code ends here

#Abort function defination
def abort_if_date_doesnt_exist(date):
    if not any(d["DATE"]==date for d in res2):
       abort(404,message="DATE doesn't exist".format(date))

#forecast function
def forecast(date):
    if any(d["DATE"]==date for d in res2):
       match=next((l for l in res2 if l['DATE'] == date), None)
       z=[match["TMAX"],match["TMIN"]]
    else:
       z=[]
       da=[]
       yy=int(date[0:4])
       mm=int(date[4:6])
       dd=int(date[6:8])
       date=datetime.datetime(yy,mm,dd)
	   i=date.timetuple().tm_yday
	   z.append(yntmax[i])
	   z.append(yntmin[i])
    return z

## WList
## shows a list of all Weather Dates available
class WList(Resource):
    def get(self):
        res1.sort(key=operator.itemgetter("DATE"))
        return res1, 200

    def post(self):
      json_data=request.get_json(force=True)
      date_1=json_data["DATE"]
      tmax_1=json_data["TMAX"]
      tmin_1=json_data["TMIN"]
      if any(d["DATE"]==date_1 for d in res1):
         match_1=next((l for l in res2 if l["DATE"]==date_1),None)
         res2.remove(match_1)
         match_2=next((l for l in res1 if l["DATE"]==date_1),None)
         res1.remove(match_2)
      res1.append({"DATE":date_1})
      res2.append({"DATE":date_1,"TMAX":tmax_1,"TMIN":tmin_1})
      match_2=next((l for l in res1 if l["DATE"]==date_1),None)
      return match_2, 201

##Wdate
##Relating to Wdate Resource
class Wdate(Resource):
    def get(self,date):
       abort_if_date_doesnt_exist(date)
       match=next((l for l in res2 if l["DATE"]==date),None)
       return match, 200

    def delete(self,date):
       abort_if_date_doesnt_exist(date)
       match=next((l for l in res2 if l["DATE"]==date),None)
       res2.remove(match)
       match=next((l for l in res1 if l["DATE"]==date),None)
       res1.remove(match)
       return "Successfully deleted", 200

##Wforecast
class Wforecast(Resource):
    def get(self,date):
        res3=[]
        da=[]
        da.append(date)
        ff=[]
        yy=int(date[0:4])
        mm=int(date[4:6])
        dd=int(date[6:8])
        date=datetime.datetime(yy,mm,dd)
		for i in range(6):
			date+=datetime.timedelta(days=1)
				da.append(datetime.date.strftime(date,"%Y%m%d"))
        for i in range(0,7):
			ff.append(forecast(da[i]))
        for i in range(0,7):
			res3.append({"DATE":da[i],"TMAX":ff[i][0],"TMIN":ff[i][1]})
       return res3, 200
	   
##Wuforecast
class Wuforecast(Resource):
    def get(self,date):
		wutmax=[]
		wutmin=[]
	    da=[]
        da.append(date)
        ff=[]
        yy=int(date[0:4])
        mm=int(date[4:6])
        dd=int(date[6:8])
        date=datetime.datetime(yy,mm,dd)
		current=datetime.datetime.now()
                diff=current-datetime.timedelta(days=6)
                if date.date()<diff.date():
                        for i in range(6):
                                date+=datetime.timedelta(days=1)
                                da.append(datetime.date.strftime(date,"%Y%m%d"))
                        for i in range(7):
                                url = "http://api.wunderground.com/api/b6975a61beac7f95/history_"+da[i]+"/q/OH/Cincinnati.json"
                                response = urllib.urlopen(url)
                                data = json.loads(response.read())
                                wutmax.append(float(data['history']['dailysummary'][0]['maxtempi']))
                                wutmin.append(float(data['history']['dailysummary'][0]['mintempi']))
                elif date.date()>=diff.date():
                        q=current-date
                        p_range=abs(q.days)
                        for i in range(p_range):
                                date+=datetime.timedelta(days=1)
                                da.append(datetime.date.strftime(date,"%Y%m%d"))
                        for i in range(p_range):
                                url = "http://api.wunderground.com/api/<yourKeyID>/history_"+da[i]+"/q/OH/Cincinnati.json"
                                response = urllib.urlopen(url)
                                data = json.loads(response.read())
                                wutmax.append(float(data['history']['dailysummary'][0]['maxtempi']))
                                wutmin.append(float(data['history']['dailysummary'][0]['mintempi']))
                        url = "http://api.wunderground.com/api/<yourKeyID>/forecast10day/q/OH/Cincinnati.json"
                        response = urllib.urlopen(url)
                        data = json.loads(response.read())
                        for i in range (7-p_range):
                                wutmax.append(float(data['forecast']['simpleforecast']['forecastday'][i]['high']['fahrenheit']))
                                wutmin.append(float(data['forecast']['simpleforecast']['forecastday'][i]['low']['fahrenheit']))
                elif date.date()==current.date():
                        url = "http://api.wunderground.com/api/<yourKeyID>/forecast10day/q/OH/Cincinnati.json"
                        response = urllib.urlopen(url)
                        data = json.loads(response.read())
                        for i in range (7):
                                wutmax.append(float(data['forecast']['simpleforecast']['forecastday'][i]['high']['fahrenheit']))
                                wutmin.append(float(data['forecast']['simpleforecast']['forecastday'][i]['low']['fahrenheit']))
		else:
			abort_if_date_doesnt_exist(date)
		res4={"wutmax":wutmax,"wutmin":wutmin}
		return res4,200
	
@app.route('/')
def home():
        return render_template('home.html')



##
## Actually setup the Api resource routing here
##
api.add_resource(WList, '/historical/')
api.add_resource(Wdate, '/historical/<date>')
api.add_resource(Wforecast, '/forecast/<date>')
api.add_resource(Wuforecast,'/wuforecast/<date>')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)
