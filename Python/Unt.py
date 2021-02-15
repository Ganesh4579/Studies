g=input("Sm")
try:
    r=open(g)
except:
    print('v')
    exit()

for i in r:
   
    if i.startswith('M'):
        i=i.rstrip()
        print(i)
   
    
        

    

    
