import pandas as pn
import numpy as nu

d=pn.read_csv('poly.csv')
X=d.iloc[:,0:1]
y=d.iloc[:,1]

from sklearn.preprocessing import PolynomialFeatures
pol=PolynomialFeatures(degree=6)
Xp=pol.fit_transform(X)

from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(Xp,y)
reg1=LinearRegression()
reg1.fit(X,y)

from matplotlib import pyplot as py
py.scatter(X,y)
py.plot(X,reg.predict(Xp))
py.show()