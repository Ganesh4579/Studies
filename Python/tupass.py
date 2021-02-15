f=open("Sm.txt")
s=f.read()
d=dict()
v=s.split()
for i in v:
    d[i]=d.get(i,0)+1  
z=sorted([(j,k) for (k,j) in d.items()],reverse=True)

print(z)
for i in z:
    print('')
    for j in i[::-1]:
        print(j,end=' ')
