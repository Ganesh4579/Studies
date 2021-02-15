from sklearn import datasets
import sklearn.datasets
BC=datasets.load_breast_cancer()

from sklearn.model_selection import train_test_split
Xtr,Xte,ytr,yte=train_test_split(BC.data,BC.target,train_size=.9,stratify=BC.target,random_state=0)

from sklearn.linear_model import LogisticRegression
mo=LogisticRegression()
mo.fit(Xtr,ytr)

from sklearn.metrics import accuracy_score
print(accuracy_score(ytr,mo.predict(Xtr)))
print(accuracy_score(yte,mo.predict(Xte)))


import numpy as np
p=(13.54,14.36,87.46,566.3,0.09779,0.08129,0.06664,0.04781,0.1885,0.05766,0.2699,0.7886,2.058,23.56,0.008462,0.0146,0.02387,0.01315,0.0198,0.0023,15.11,19.26,99.7,711.2,0.144,0.1773,0.239,0.1288,0.2977,0.07259)
p=np.array(p)
p=p.reshape(1,-1)
ps=mo.predict(p)
print('The breast Cancer is Malignant' if ps==0 else 'The breast cancer is Benign' )