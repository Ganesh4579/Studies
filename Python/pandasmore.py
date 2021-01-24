import pandas as pd

df=pd.DataFrame({'A' :[1,2,3,4],'B':[5,6,7,8],'C':[2,5,5,2],'D':['q','s','q','s']})

print(df[df.A>=3]['B'])
print(df[df.columns[1]])

import numpy as np
dfd=pd.DataFrame(np.random.randint(30,100,size=(100,4)))
print((df))
print(u'~ello\n\n')

#df=df.applymap(float)
#print(df)

ds=df.groupby(['D','C']).A.max()
print(ds.index)
print(ds)

print(ds.loc[:,5])

print(df[df.notnull()])
#print(df.get_loc(6))