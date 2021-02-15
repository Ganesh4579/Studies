u=int(input('e'))
def f(n):
    if n<0:
        return n
    elif n==0 or n==1:
        return n
    else:
        t=1
        while(n>1):
            t=t*n
            n=n-1
    return t

print(f(u))