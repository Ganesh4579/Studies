import mysql.connector as mc
import pandas as pn
import matplotlib as mp

my=mc.connect(
    host='localhost',
    user='root',
    passwd='4579'
)
cur=my.cursor()

cur.execute('use base')
cur.execute('select * from employee')
x=cur.fetchall()

d=pn.DataFrame(x)
#for i in x:
    #d.append(i)
print(d)
print(d.info())
print(d.describe())
print(d[4].value_counts())

d[0].plot(kind='pie',figsize=(6,6))
#print(d.loc(d[4]=='M'))