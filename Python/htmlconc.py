import mysql.connector as mc
import pandas as pn
import matplotlib.pyplot as mp
import numpy as np

import ssl

ssl._create_default_https_context = ssl._create_unverified_context
ht=pn.read_html('https://en.wikipedia.org/wiki/List_of_Marvel_Cinematic_Universe_films')
#db=pn.concat(ht)
db=ht[1]
db.dropna(axis=1,inplace=True)
#print(db)
#print(db.isna().count())
print(db.shape[0]+1)
print(len(db))
