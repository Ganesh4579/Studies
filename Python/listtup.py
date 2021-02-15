l,q=list(),list()
while True:
    t=input('enter the number')
    if t=='e':
        break 
    else :
        l.append(int(t))
print(l)
for i in l:
    m=tuple()
    m=(i,i**3)
    q.append(m)
print(q)
        
