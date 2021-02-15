di={}
li=[]
g='Madhavan signed the film in January 2002 after being impressed with Linguswamy narration and through the project, made his first appearance in an action-orientated role'
li=g.split()
for i in li:
    di[i]=di.get(i,0)+1
print(di)
di['qqqqqqqqqqq']='2'
print('\n')
print(list(di))
print('\n')
print(di.values())
f={}
print(f.get('c',-564564))
