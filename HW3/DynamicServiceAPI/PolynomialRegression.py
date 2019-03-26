from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
import numpy as np
import csv

filename="daily.csv"
rows=[]
with open(filename,'r') as csvfile:
    csvreader=csv.reader(csvfile)
    for row in csvreader:
       rows.append(row)
y=csvreader.line_num
csvfile.close()

ytmax=[]
ytmin=[]

for i in range(1463,1827):
   ytmax.append(rows[i][1])
   ytmin.append(rows[i][2])

x = np.arange(1,365)
model1 = Pipeline([('poly', PolynomialFeatures(degree=5)),
                  ('linear', LinearRegression(fit_intercept=False))])
model1 = model1.fit(x[:, np.newaxis], ytmax)
print(model1.named_steps['linear'].coef_)

yntmax=[]
for i in range(1,365):
    yntmax.append(model1.predict(i))

model2 = Pipeline([('poly', PolynomialFeatures(degree=5)),
                  ('linear', LinearRegression(fit_intercept=False))])
model2 = model2.fit(x[:, np.newaxis], ytmin)
print(model2.named_steps['linear'].coef_)
yntmin=[]
for i in range(1,365):
    yntmin.append(model2.predict(i))
    
