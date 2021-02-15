def par(q,s,e):
    i=s-1
    p=q[e]
    for j in range(s,e):
        if p>=q[j]:
            i+=1
            q[i],q[j]=q[j],q[i]
    q[e],q[i+1]=q[i+1],q[e]
    return (i+1)

def qs(q,s,e):
    if s<e:
        pi=par(q,s,e)
        qs(q,s,pi-1)
        qs(q,pi+1,e)



q=[10, 7, 8, 9, 1, 5,4,7,4,7,4,6,0,3,5,7,2,5,2]
qs(q,0,len(q)-1)
print(q) 