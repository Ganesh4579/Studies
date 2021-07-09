def arm(a):
    l=len(str(a))
    t=0
    for i in str(a):
        t+=int(i)**l
    if t==a:
        return True
    
e=int(input('enter'))
if arm(e):
    print('s')
else:
    print('n')
 