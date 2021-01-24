from sklearn.preprocessing import OneHotEncoder

x = [[11, "Spain"], [22, "France"], [33, "Spain"], [44, "Germany"], [55, "France"]]
y = OneHotEncoder().fit_transform(x).toarray()
print(y)

from sklearn.preprocessing import LabelBinarizer

y = LabelBinarizer().fit_transform(x)
print(y)#doesn't support multi class