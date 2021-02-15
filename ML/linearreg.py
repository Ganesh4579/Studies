from matplotlib import colors
from matplotlib.pyplot import show, xlabel
from numpy import random
import numpy
from numpy.core.defchararray import array

ages=[random.randint(20,65) for i in range(60)]
networth=[j*6.25+random.normal(scale=40) for j in ages]
ages=numpy.reshape(numpy.array(ages),(len(ages),1))
networth==numpy.reshape(numpy.array(networth),(len(networth),1))



from sklearn.model_selection import train_test_split
a_tr,a_te,n_tr,n_te=train_test_split(ages,networth)



def lrm(a,b):
  from sklearn.linear_model import LinearRegression
  lr=LinearRegression()
  lr=lr.fit(a,b)
  return lr


lr=lrm(a_tr,n_tr)

print('slope',lr.coef_)
print('intercept',lr.intercept_)

print('test',lr.score(a_te,n_te))
print('train',lr.score(a_tr,n_tr))

for k in n_te:
      for l in lr.predict(a_te):
            print(k,'        ',l)
            
print(lr.predict([[61]]))
  

import matplotlib.pyplot as plt
plt.plot(a_te,lr.predict(a_te))
plt.scatter(ages,networth)
plt.xlabel("Ages")
plt.ylabel("Net Worth")
plt.show()



