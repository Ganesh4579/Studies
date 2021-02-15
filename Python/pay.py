a=[]
sum=0
count=0
average=0
while True:
    a=input('Enter numbers')

    if(a=='exit'):
            break
    try:
        u=int(a)
    except:
        print('Not a number')
        continue
    sum=sum+u
    count=count+1
    average=sum/count
print('Sum is',sum)
print('count is',count)
print('Average is',average)







