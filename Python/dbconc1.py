import mysql.connector as mc


my=mc.connect(
    host='localhost',
    user='root',
    passwd='4579'
)
cur=my.cursor()

cur.execute('use base')
cur.execute('select * from employee')
x=cur.fetchall()

for i in x:
    print(i)