l=list()
s={'q':2,'g':7,'a':9}
#t=sorted([(j,i) for (i,j) in s.items()])



for (i,j) in s.items():
    l.append((i,j))
l=sorted(l,reverse=True)   
print(l)
print('\n')
t=(1,4,6,6,8,4,7)
print(t[1:3])
