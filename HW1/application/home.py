from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/home')
def home():
   return render_template('home.html')

@app.route('/result', methods = ['POST','GET'])
def result():
   if request.method=='POST':
    result = request.form
    x = int(request.form['x'])
    y = [2]
    for i in range(3,x):
      for j in range(2,i-1):
         if i%j==0:
            flag=0
            break
      else:
            flag=1
      if flag:
       y.append(i)
    res=[]
    for i in range(0,len(y)):
          if y[i]<10:
             continue
          else:
             a=1
             b=1
             lfr=[]
             rfl=[]
             while(y[i]/(10**a)!=0):
               lfr.append(y[i]%(10**a))
               a+=1
             while(y[i]/(10**b)!=0):
               rfl.append(y[i]/(10**b))
               b+=1
          l=0
          while(l<len(lfr)):
             if lfr[l] not in y:
               fl1=0
               break
             else:
               fl1=1
             l+=1
          m=0
          while(m<len(rfl)):
             if rfl[m] not in y:
               fl2=0
               break
             else:
               fl2=1
             m=m+1
          if fl1 and fl2:
             res.append(y[i])
   return render_template('result.html',res=res,x=x)


if __name__ == "__main__":
    app.run(ssl_context=('cert.pem','key.pem'))


