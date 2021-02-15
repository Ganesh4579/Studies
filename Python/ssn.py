n=int(input('e'))
p=0
s=0
for i in range(n+1):
    t=i**2
    s=p+t
    p=s
    
print(p)