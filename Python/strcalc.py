s="::::::PythoNProgramming@PerfectPlanB111222333:::::"
l=0
u=0
y=0
d=0
for i in s:
      if(i.islower()):
            l+=1
      elif(i.isupper()):
            u+=1
      elif(i.isnumeric()):
            d+=1
      else:
            y+=1
print(l+u,l,u,d,y)
            