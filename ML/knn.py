import pandas as p
import numpy as n

d=p.read_csv('knn.csv')
from sklearn.model_selection import train_test_split
Xtr,Xte,ytr,yte=train_test_split(d[['hei','age']],d.wei,train_size=.8)

from sklearn.neighbors import KNeighborsClassifier
k=KNeighborsClassifier(n_neighbors=6)
k=k.fit(Xtr,ytr)
print(k.score(Xtr,ytr))

print(k.predict(Xte))
from sklearn.metrics import accuracy_score
print(accuracy_score(yte,k.predict(Xte)))