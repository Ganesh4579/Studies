import numpy as np

l=np.random.randint(10,30,40)
l=list(l)
d=dict()

for i in l:
    d[i] =d.get(i,0)+1
#s=dict(sorted(d.items(),reverse=True,key=lambda x: x[1]))   #by value
s=dict(sorted(d.items(),reverse=True,key=lambda x: x[0]))    #by key
print(s)

# OR
d1=dict()
for i in sorted(l):
    if i not in d1:
        d1[i]=1
    else:
        d1[i]+=1
#print(d1)

