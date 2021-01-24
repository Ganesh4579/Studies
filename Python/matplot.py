import mysql.connector as mc
import pandas as pn
import matplotlib.pyplot as mp
import numpy as np

fig=mp.figure(figsize=(12,6))
fig.suptitle("Empty figure")
axe = fig.add_subplot(1,1,1)
# Set the title of plot
axe.set_title("Empty plot")
#mp.show()

fi, ar_ax = mp.subplots(2, 2)
mp.show()

