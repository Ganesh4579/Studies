from os import read


f=open('mt.txt')
for i in f:
    i=i.rstrip()
    i=i.split()
    #print(i[2])
    print(i)
        
    

