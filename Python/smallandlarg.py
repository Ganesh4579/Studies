l=list()
while True :
    e=input('enter')
    if (e=='e'):
        break  
    try:
        l.append(int(e))
    except:
        break
print(l)
t=0
for i in l:
    if (i>t):
         t=i 
print('l is ',t)
t=0
for i in l:
    if t==0:
        t=i
    elif i<t:
        t=i
    else:
        continue
print('s is ',t)