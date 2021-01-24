import mysql.connector as mc
import pandas as pn
import matplotlib as mp
import numpy as np

my=mc.connect(
    host='localhost',
    user='root',
    passwd='4579'
)
cur=my.cursor()

A = np.array([
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
])

B= np.array(['a', 'b', 'c'])

q=np.arange(0,7,2)
print(q)
w=np.linspace(0,7,2)
print(w)
e=np.random.randn(2,7)
print(e)


qw=np.eye(5)
print(qw)