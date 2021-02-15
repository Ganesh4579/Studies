q=[10, 20,5, 80,72, 30, 60,10, 50,110, 100, 130,40, 70,20]
q.sort()
print(q)
s=int(input('e'))
def binr(q,s,l,h):
    
    if l<=h:
        m=(l+h)//2
        if q[m]<s:
            return binr(q,s,m+1,h)
        elif q[m]>s:
            return binr(q,s,l,m-1)
        else:
            return m
    else:
        return -1
re=binr(q,s,0,len(q)-1)
print(re)
if(re==-1):
    print('n')
else:
    print('s')
        