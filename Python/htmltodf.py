import mysql.connector as mc
import pandas as pn
import matplotlib.pyplot as mp
import numpy as np

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

ht=pn.read_html('https://github.com/ine-rmotr-curriculum/RDP-Reading-Data-with-Python-and-Pandas/raw/master/unit-1-reading-data-with-python-and-pandas/lesson-18-get-fifa-players-from-the-web/files/fifa_players.html')
db=pn.concat(ht)
db.dropna(axis=1,inplace=True)
print(db)
print(db.isna().count())
