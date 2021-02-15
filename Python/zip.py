a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)

#use the tuple() function to display a readable version of the result:

print(tuple(x),'\n')

c=[(i,j) for i,j in zip(a,b)]
      
print(c)