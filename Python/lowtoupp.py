s=input('e')
l,u=list(),list()
for i in s:
      if i.islower():
            l.append(i)
      else:
            u.append(i)
for i in l:
      print(i,end='')
print()
for i in u:
      print(i,end='')

            