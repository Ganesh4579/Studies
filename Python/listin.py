l=list()
while True:
    n=(input('e'))
    if n=='e':
        break
    else:
        l.append(int(n))
print(l,'\n')
print(l[-1])
t=l[0]
l[0]=l[len(l)-1]
l[len(l)-1]=t
print(l)
print(l[-1])
        
        
    