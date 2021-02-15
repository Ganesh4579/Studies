l=int(input('l'))
u=int(input('u'))


for i in range(l,u+1):
    if(i>1):
        for j in range(2,i):
            if((i%j)==0):
                break
            else:
                if(j==i-1):
                    print(i)
                    break
                
    
        
      
            
        
       
