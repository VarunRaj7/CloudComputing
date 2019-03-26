from flask import Flask,request
from flask_restful import reqparse, abort, Api, Resource
import json
import csv
import datetime
import operator

app = Flask(__name__)
api = Api(app)

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

def abort_if_date_doesnt_exist(date):
    if not any(d["DATE"]==date for d in res2):
       abort(404,message="DATE doesn't exist".format(date))

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
       for i in range(2):
          date+=datetime.timedelta(days=-1)
          da.append(datetime.date.strftime(date,"%Y%m%d"))
       if any(d["DATE"]==da[0] for d in res2):
          match=next((l for l in res2 if l['DATE'] == da[0]), None)
          p=[match["TMAX"],match["TMIN"]]
       else:
          p=forecast(da[0])
       if any(d["DATE"]==da[1] for d in res2):
          match=next((l for l in res2 if l['DATE'] == da[1]), None)
          q=[match["TMAX"],match["TMIN"]]
       else:
          q=forecast(da[1])
       for i in range(0,2):
          z.append((p[i]+q[i])/2) ## Moving Average
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
       if date<="20180228":
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
       else:
          abort(404,message="Can't Forecast for the provided date with information available".format(date))
       return res3, 200
##
## Actually setup the Api resource routing here
##
api.add_resource(WList, '/historical/')
api.add_resource(Wdate, '/historical/<date>')
api.add_resource(Wforecast, '/forecast/<date>')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=80)
