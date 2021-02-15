import re
s=open("mt.txt",'r')
for i in s:
    i=i.rstrip()
    if re.search('from+',i):
        print(i)
