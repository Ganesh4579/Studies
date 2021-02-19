#f=open("Sm.txt")
#Ws=f.read()
s='Shift left by pushing zeros in from the right and let the leftmost bits fall off'
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
