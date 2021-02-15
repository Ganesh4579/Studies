import math
from matplotlib import colors
from matplotlib.pyplot import show, xlabel
from numpy import random
import numpy
from numpy.core.defchararray import array
from numpy.core.fromnumeric import shape
import pandas as pa
import math

xl=pa.read_csv('Book.csv')
xl.wei=xl.fillna(math.floor(xl.wei.median()))
tr=xl[['vol','wei']]
te=xl['co2']
from sklearn.model_selection import train_test_split
X_tr,X_te,co2_tr,co2_te=train_test_split(tr,te)

def lrm(a,b):
    from sklearn.linear_model import LinearRegression
    lr=LinearRegression()
    lr=lr.fit(a,b)
    return lr

lr=lrm(X_tr,co2_tr)


print('slope',lr.coef_)
print('intercept',lr.intercept_)

print('test',lr.r2_score(X_te,co2_te))
print('train',lr.r2_score(X_tr,co2_tr))

print('ln',lr.predict([[1300,1120]]))