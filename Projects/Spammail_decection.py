from ast import iter_fields
import pandas as pn
dt=pn.read_csv('/home/ganesh/Documents/Projects/spamham.csv')

X=dt.Message
y=dt.Category

y.loc[y=='spam',]=0
y.loc[y=='ham',]=1
y=y.astype('int')

from sklearn.model_selection import train_test_split
Xtr,Xte,ytr,yte=train_test_split(X,y)

from sklearn.feature_extraction.text import TfidfVectorizer
fe=TfidfVectorizer(min_df=1,stop_words='english',lowercase='True')
Xtr=fe.fit_transform(Xtr)
Xte=fe.transform(Xte)
Xtr=Xtr.astype('int')
Xte=Xte.astype('int')

from sklearn.svm import SVC
mo=SVC()
mo.fit(Xtr,ytr)

from sklearn.metrics import accuracy_score
print(accuracy_score(ytr,mo.predict(Xtr)))
print(accuracy_score(yte,mo.predict(Xte)))

it=["I've been searching for the right words to thank you for this breather. I promise i wont take your help for granted and will fulfil my promise. You have been wonderful and a blessing at all times."]
it=fe.transform(it)
print('spam' if mo.predict(it)==0 else 'ham')
