def fib(a):
    if a==0 :
            print(0)
    elif a==1 :
            print(1)
    else:
        n1,n2=0,1
        for i in range(a):
            print(n1)
            n1=n2
            t=n1+n2
            n2=t
            

e=int(input('enter'))
fib(e)