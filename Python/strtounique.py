s=input('e')
c=0
for i in s:
      for j in s[s.index(i)+1:len(s)]:
            if i==j:
                  print('n')
                  c+=1
                  break
      if(c==1):
            break
if(c!=1):
      print('s')    

               

      