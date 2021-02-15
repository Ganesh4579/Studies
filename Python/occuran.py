l = ["can", "you", "can", "a", "can","?",'a']
s=set(l)
print(s,'\n')
w='can'
c=0
for i in l:
    if w==i:
        c=c+1
    
        if c>1:
            l.pop(l.index(i))
print(l,c)
        