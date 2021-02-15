import numpy
import pandas
import numpy as n
d=pandas.read_csv('class.csv')
from sklearn.model_selection import train_test_split
age=numpy.array(d.age)
age=age.reshape(len(age),1)
Xtr,Xte,ytr,yte=train_test_split(age,d.ins,train_size=.8)


from matplotlib import pyplot as p
p.scatter(Xtr,ytr,marker='+',color='red')
p.show()


from sklearn.linear_model import LogisticRegression
r=LogisticRegression()
r=r.fit(Xtr,ytr)

print(r.score(Xte,yte))
print(r.predict([[38]]))