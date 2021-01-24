import pandas as pd
import numpy as np

a=np.arange(100,110)
ds=pd.Series(a,name='roll_no',index=range(1,10+1))

print(ds)

c=['tam','eng','mat','sci']
import pandas as pd

s=pd.DataFrame(np.random.randint(30,100,size=(10,4)),columns=c)
print(s) 

s.index=ds
#s[ds.name]=ds.values
#s.index=s[ds.name]
s

d=np.random.randint(30,100,size=4)
dd=zip(c,d)
dd=dict(dd)
#s=s.append(d,ignore_index=True)