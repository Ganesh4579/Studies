g=input("Sm")
try:
    r=open(g)
except:
    print('v')
    exit()

for i in r:
   
    if i.startswith('m'):
        i=i.rstrip()
        print(i)
   
    
        

    

    
