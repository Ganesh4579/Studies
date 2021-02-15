f=open('Sm.txt')
s=f.read()
d=dict()
q=s.split()
for j in q:
     d[j]=d.get(j,0)+1
print(d)
t=-1
for k in d:
    if(d[k]>t):
        t=d[k]
        m=k
print(m,'comes',t,'times')
