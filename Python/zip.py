a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)

#use the tuple() function to display a readable version of the result:

print(tuple(x),'\n')

c=[(i,j) for i,j in x]
      
print(c)
from collections import deque
la=deque([1,1,1,1,1,1],10)