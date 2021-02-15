from numpy import random
import numpy
from numpy.core.defchararray import array

ages=[random.randint(20,65) for i in range(60)]
networth=[j*6.25+random.normal(scale=40) for j in ages]


from scipy import stats
sl,inc,r,p,err=stats.linregress(ages,networth)

def cal(a):
    return sl*a+inc
print(r)
print(cal(41))