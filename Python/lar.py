t=-1
while True:
    n=input('e')
    if(n=='e'):
        break
    else:
        n=int(n)
        if n>t:
            t=n
print(t)