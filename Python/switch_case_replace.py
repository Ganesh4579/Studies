def sw(a):
    d={1:'one',2:'two'}
    return d.get(a,0)

e=int(input('enter'))
print(sw(e))