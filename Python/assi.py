def calc(a,b):
   return a+b,a-b
a=int(input('a'))
b=int(input('b'))
print(calc(a,b))
print('\n\n\n\n')

def rec(n):
    if n:
        return n+rec(n-1)
    else:
        return 0
n=10
print(rec(n))
print('\n\n\n\n')
for i in range(4,30):
    if i%2==0:
        print(i)
#print('\n\n\n\n')
#print(list(range(4,30,2)))
#aList = [4, 6, 8, 24, 12, 2]
#print(max(aList))
