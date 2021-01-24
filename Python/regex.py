with open('test.txt') as t:
    s=t.readline()
    t.close()

import re
print(s)

#w=re.findall('*ine',s)
'''w=re.finditer('This','This d uuui This')
for i in w:
    print(i)
print(w)'''
q='sat,hat,mat,pat'
d=re.findall('[^h-m]at',q)
#print(d)
q=re.sub(pattern='sat',repl='Sat',string=q)
print(q)

print(re.search(r'hat',q))

