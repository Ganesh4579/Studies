l=list()
while True:
    n=input("e")
    if n=='e':
        break
    else:
        l.append(n)
print(l)
q=int(input('s1'))
w=int(input('s2'))
l[q],l[w]=l[w],l[q]
print(l,'\n')
e=int(l.pop(w))
r=int(l.pop(q))
l.insert(q,e)
l.insert(w,r)
print(l)
  