s=input('e')
c=0
print(len(s))
for i in range(0,len(s)):
    if s[i]==s[len(s)-i-1]:
        c+=1
if c==len(s):
    print('s')
else:
    print('n')
        