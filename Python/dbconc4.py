import mysql.connector as mc
import pandas as pn
import matplotlib as mp
import numpy as np

my=mc.connect(
    host='localhost',
    user='root',
    passwd='4579',
    database='base'
)

db=pn.read_sql('select * from employee',my,index_col='emp_id',columns=['first_name','last_name','birth_day','salary','sex','super_id','branch_id'])
#db.index=[np.arange(101,110)]
db.drop('sex',axis=1)

#print(db['sex'])
#print(db.iloc[2:5,5])
#print(db.loc[4,['sex','emp_id']])

#data cleaning
db['birth_day']=pn.to_datetime(db['birth_day'])
#print(db['birth_day'].head(2))
#db.set_index(db['emp_id'],inplace=True)
print(db)
print(db.index)
print(db.loc[104])




print('\n\n\n\n',db.shape[1:7])
