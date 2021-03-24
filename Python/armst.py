n=int(input('e'))
s=str(n)
d=len(str(n))
t=0
for i in s:
    t=t+int(i)**d
if t==n:
    print('s')
else:
    print('n')
    
dir(len)
