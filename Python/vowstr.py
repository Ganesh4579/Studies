s=input('e')
s=s.lower()
v=('aeiou')
s1=set()
for i in s:
    if i in v:
        s1.add(i)
if len(s1)==len(v):
    print('s')
else:
    print('n')
    

        
        
           
        