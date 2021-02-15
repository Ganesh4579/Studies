from os import read


f=open('md.txt')
f=f.read()
print(f,'\n\n')
t=f.split('\n')
for i in t:
      if t.index(i)%2==0:
            print(i)
      
