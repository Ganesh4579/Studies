w='perfectplanb'
d={}
for i in w:
   d[i]=d.get(i,0)+1
print(d)
s={'p':1,'pl':42,'b':100}
for k in s:
    
    if(s[k]>10):
        print(k,s[k])
    