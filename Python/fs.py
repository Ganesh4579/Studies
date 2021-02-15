import math
n=int(input('e'))

def sqrn (num):
    c=int(math.sqrt(num))
    return c*c==num

def sq(n):
    return sqrn(5*n**2+4) or  sqrn(5*n**2-4) 

print (sq(n))