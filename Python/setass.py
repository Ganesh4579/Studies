l='1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 '
s=l.split()
d=dict()
for i in s:
    d[i]=d.get(i,0)+1
print(d)
for i,j in d.items():
    if j==1:
        print(i)
      