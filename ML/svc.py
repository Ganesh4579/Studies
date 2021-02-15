from math import gamma
from sklearn.datasets import load_iris
from sklearn.utils.validation import column_or_1d
i=load_iris()

import pandas as pn
import numpy as n

d=pn.DataFrame(i.data,columns=i.feature_names)

d['target']=i.target
d['flower_names']=d.target.apply(lambda x:i.target_names[x])

d0=d[0:50]
d1=d[50:100]
d2=d[100:]

from matplotlib import pyplot as py
py.subplot(1,2,1)
py.xlabel('sepal length (cm)')
py.ylabel('sepal width (cm)')
py.scatter(d0['sepal length (cm)'],d0['sepal width (cm)'],color="red",marker="+")
py.scatter(d1['sepal length (cm)'],d1['sepal width (cm)'],color="blue",marker="*")


py.subplot(1,2,2)
py.xlabel('Petal Length')
py.ylabel('Petal Width')
py.scatter(d0['petal length (cm)'], d0['petal width (cm)'],color="green",marker='+')
py.scatter(d1['petal length (cm)'], d1['petal width (cm)'],color="blue",marker='.')
py.show()

X=d.drop(['target','flower_names'],axis='columns')
y=d.target

from sklearn.model_selection import train_test_split
Xtr,Xte,ytr,yte=train_test_split(X,y,train_size=.8,random_state=1) 

from  sklearn.svm import SVC
s=SVC()
s=s.fit(Xtr,ytr)

print(s.score(Xte,yte))

d = SVC(C=1,kernel='linear',gamma=2)
d.fit(Xtr, ytr)
print(d.score(Xte, yte))