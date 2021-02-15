import pandas as pn
d=pn.read_csv('titanic.csv')
di=d.drop(['PassengerId','Name','SibSp','Parch','Ticket','Cabin','Embarked','Survived'],axis='columns')
dt=d['Survived']


from sklearn.preprocessing import LabelEncoder
disex=LabelEncoder()
di['sexn']=disex.fit_transform(di['Sex'])
di=di.drop(['Sex'],axis='columns')
di=di.fillna(int(di.Age.median()))

from sklearn.model_selection import train_test_split
Xtr,Xte,ytr,yte=train_test_split(di,dt,random_state=0,test_size=.3)



from sklearn.tree import DecisionTreeClassifier
re=DecisionTreeClassifier()
re.fit(Xtr,ytr)

print(re.score(Xte,yte))