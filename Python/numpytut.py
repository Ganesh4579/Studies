# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np

f=np.array(range(10),ndmin=3)
print(f)
print(f.shape)
print(f.ndim)

c=f.copy()
v=w.view()
f[0]=1000000
c.base
print(v)


# %%
for i in np.ndenumerate(f):
    print(i)


# %%
np.random.random(45)


# %%
np.add(f,c)


# %%
np.empty(2)


# %%
np.repeat(f,2,axis=0)


# %%
np.isnan(f).sum()


# %%



