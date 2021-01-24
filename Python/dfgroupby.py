
import pandas as pd 
  
# sample dataframe 
df = pd.DataFrame({ 'A': ['foo', 'bar', 'g2g', 'g2g', 'g2g', 
                                'bar', 'bar', 'foo', 'bar'], 
                   'B': ['a', 'b', 'a', 'b', 'b', 'b', 'a', 'a', 'b'] }) 
  
# Multi-column frequency count 
#count = df.groupby(['A']).count() 
#print(count) 
ds=df.groupby('A')
for i,j in ds:
    print(f'{i}\n{j}')
print(ds.get_group('foo'))
d=pd.get_dummies(df['A'])
hj=pd.concat([df,d],axis=1)
print(hj.index)
print(df.append(d,sort=False,ignore_index=True))

#didx = pd.DatetimeIndex(start ='2014-08-01 10:05:45', freq ='D', periods = 5, tz ='Asia/Calcutta') 
                               
'''print(didx)
print(didx.date)
print(didx.month)'''
#print(df.loc[: ,'B'])

ps=df['A'].value_counts().to_frame()
print(ps)

import matplotlib.pyplot as mp

ps.plot(kind='box')
mp.show()

io=pd.DataFrame({'a':[1,2,3,'q']})
#io.astype({'a':'int64'})
print(io['a'].apply(type).value_counts())
