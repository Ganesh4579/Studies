import math

def fibc(a):
    ps1,ps2=int(math.sqrt((5*(a**2))-4)),int(math.sqrt((5*(a**2))+4))
    if ps1**2==((5*(a**2))-4) or ps2**2==((5*(a**2))+4):
        print('s')
    else :
        print('n')

e=int(input('enter'))
fibc(e)