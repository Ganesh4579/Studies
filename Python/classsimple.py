class a():
    __c=6666
    def __init__(self):
        print('got excuted')
    def f(self,s):
        #print(a.c,s)
        pass
x=a()
x.f(3)
print(a.c)