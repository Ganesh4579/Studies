import mysql.connector as mc
import pandas as pn
import matplotlib as mp
import numpy as np

db=pn.read_csv('ex.csv')

print(db.head())
print(db.describe())
print(db.info())

db.set_index(np.arange(100,114),inplace=True)
print(db.index)


dm=pn.Series([2,5,2,np.nan,'sd'])
#print(dm.values)


db.rename(columns={'Age':'age'},inplace=True)

#db.drop(104,inplace=True,axis=0)
#print(db)
#print(db.loc[db.index >105,'age'])
#print(db.iloc[4:7])

db.loc[104,'Name']='oooo'
db.loc[120,'Name']='sfd'

db.loc[db['age']>100,'age'] /= int(10)

#print(db['Sex'].value_counts())
db.loc[(db['Sex']!="m") & (db['Sex']!="f"),'Sex']='m'

db['age'].astype='int64'
db['age'].fillna(int(round(db['age'].mean())),inplace=True)
db['Sex'].fillna(method='ffill',inplace=True)
#print(db)
#print(db.loc[104,['age','Sex']])

db.loc[107,'Name']="oooo"
#print(db['Name'].duplicated())
print(db['Name'].str)


print(db.isna().sum())
