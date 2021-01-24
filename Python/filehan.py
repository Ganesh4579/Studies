with open('test.txt','w+') as f:
    f.mode='w+'
    for i in range(100):
        f.write('This is new line {} of text to test\n'.format(i))
f=open('test.txt','a+')
print(f)
print(f.mode)
#print(f.readlines())
f.seek(0)
f.write('Thank You')
f.seek(0)
d=f.read()
print(d)
print(d.startswith('Th'))
f.close()