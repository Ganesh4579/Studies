import pandas as pn
import numpy as nu

d=pn.read_csv('total_data.csv')
X=d[['match','runs']]
X=X[X.match!=0 ]


from sklearn.preprocessing import MinMaxScaler
m=MinMaxScaler()
m.fit(X[['match']])
X['match']=m.fit_transform(X[['match']])

m.fit(X[['runs']])
X['runs']=m.fit_transform(X[['runs']])

from matplotlib import pyplot as py
#py.scatter(X.match,X.runs)
#py.show()  

s=[]
from sklearn.cluster import KMeans
for i in range(1,15):
    m=KMeans(n_clusters=i)
    m.fit(X[['match','runs']])
    s.append(m.inertia_)

m1=KMeans(n_clusters=5)
X['cl']=m1.fit_predict(X[['match','runs']])

df1=X[X.cl==0]
df2=X[X.cl==1]
df3=X[X.cl==2]
df4=X[X.cl==3]
df5=X[X.cl==4]

ol=m1.predict([[13,200]])
print(ol)
py.scatter(df1.match,df1.runs,color='red',label='runs')
py.scatter(df2.match,df2.runs,color='blue',label='runs')
py.scatter(df3.match,df3.runs,color='orange',label='runs')
py.scatter(df4.match,df4.runs,color='purple',label='runs')
py.scatter(df5.match,df5.runs,color='yellow',label='runs')
py.scatter(m1.cluster_centers_[:,0:1],m1.cluster_centers_[:,1],marker='*',color='black',label='centroid')
py.xlabel('match')
py.ylabel('runs')
py.legend()
py.show()

