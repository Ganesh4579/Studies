#%%"
l='1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 '
s=l.split()
s1,s2=set(),set()
for i in s:
    if i not in s1:
        s1.add(i)
    else:
        s2.add(i)

s1.difference_update(s2)
print(s1)
print('room number is',s1.pop())
# %%
