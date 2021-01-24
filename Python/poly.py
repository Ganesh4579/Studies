class a():
    def sp(self):
        print('a')
class b(a):
    def sp(self):
        print('b')
class c(b):
    def sp(self):
        print('c')
        
o=c()
o.sp()