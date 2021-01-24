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
#cur.execute('select * from employee')
#x=cur.fetchall()

db=pn.read_sql('select * from employee',con=my)
print(db)
print(db.loc[db['sex']=='M','emp_id'])