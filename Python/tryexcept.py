class dc(Exception):
    def __init__(self,l):
        self.l=l
    def pri(self):
        print(l)
try:
    #p=open('sadsadsa.txt')
    raise dc('ghjgjh')
   
except Exception as e:
    print('occ',type(e).__name__,e)
#finally:
    #x=1/0