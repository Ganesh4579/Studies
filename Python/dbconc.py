import mysql.connector as mc


my=mc.connect(
    host='localhost',
    user='root',
    passwd='4579'
)
cur=my.cursor()
l=input('e')
cur.execute('use base')
#ur.execute('select * from employee')
#cur.execute('show databases')
cur.execute(l)
for i in cur:
    print(i)