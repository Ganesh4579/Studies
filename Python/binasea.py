q=[10, 20,5, 80,72, 30, 60,10, 50,110, 100, 130,40, 70,20]
q.sort()
print(q)
s=int(input('e'))
def bini(q,s):
    l=0
    h=len(q)-1
    m=0
    while l<=h:
        m=(l+h)//2
        if (q[m]<s):
            l=m+1
        elif q[m]>s:
            h=m-1
        else:
            return m
       
re=bini(q,s)
print(re)
if(re==None):
    print('n')
else:
    print('s')
       
