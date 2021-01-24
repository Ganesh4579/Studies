def pri(a):
    for i in range(2,a):
        if a%i==0:
            return False
    return True
        

e=int(input('enter'))
if pri(e):
    print('s')
else:
    print('n')
