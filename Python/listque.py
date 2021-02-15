a= [1, 2, 3, 4, 5, 6, 7]
b=[i**2 for i in a]
print(b,'\n\n\n\n')


list1 = [10, 20, 30, 40]

list2 = [100, 200, 300, 400]

for i,j in zip(list1,list2[::-1]):
    print(i,j)
print('\n\n\n\n')
 
 
l=[2,4,7,2,6,2,9,2,8,6,7,2,0]
for i in l:
    if (i==2):
        l.pop(l.index(i))
print(l)
print('\n\n\n\n')


        
           
   
