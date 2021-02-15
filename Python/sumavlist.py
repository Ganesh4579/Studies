s=[]
c=0
t=0
while True:
    e=input("ed")
    if e=="e":
        break
    e=int(e)
    s.append(e)
t=sum(s)
c=t/len(s)
    
print(t)
print(c)
            