s=int(input('size'))
for i in range(0,s+1):
    for j in range(0,i):
        print(i*'* ')
        break
print('\n')
for i in range(s,0,-1):
    for j in range(0,i):
        print(j*' ',i*'* ')
        break
print('\n')
for i in range(0,s):    
    print(" "*(s-i-1),end="")    
    for j in range(i+1):        
        print('* ',end="")    
    print()
print('\n')
for i in range(s):
    print((s-i-1)*' ',end="")
    for i in range(i+1):
        print('*',end='')
    print()
print('\n')
for i in range(s,0,-1):
    print((s-i)*' ',end="")
    for i in range(i):
        print('*',end='')
    print()


       