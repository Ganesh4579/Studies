def fac(a):
    if a==0 | a==1:
        return a
    else:
        return a*fac(a-1)
    
e=int(input('enter'))
print(fac(e))