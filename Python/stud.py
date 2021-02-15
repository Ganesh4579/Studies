
 #1. Jack's dictionary 
jack = { "name":"Jack Frost", 
         "assignment" : [80, 50, 40, 20], 
         "test" : [75, 75], 
         "lab" : [78.20, 77.20] 
       } 
         
# 2. James's dictionary 
james = { "name":"James Potter", 
          "assignment" : [82, 56, 44, 30], 
          "test" : [80, 80], 
          "lab" : [67.90, 78.72] 
        } 
  
# 3. Dylan's dictionary 
dylan = { "name" : "Dylan Rhodes", 
          "assignment" : [77, 82, 23, 39], 
          "test" : [78, 77], 
          "lab" : [80, 80] 
        } 
          
# 4. Jessica's dictionary 
jess = { "name" : "Jessica Stone", 
         "assignment" : [67, 55, 77, 21], 
         "test" : [40, 50], 
         "lab" : [69, 44.56] 
       } 
         
# 5. Tom's dictionary 
tom = { "name" : "Tom Hanks", 
        "assignment" : [29, 89, 60, 56], 
        "test" : [65, 56], 
        "lab" : [50, 40.6] 
      } 
def ave(num):
    s=sum(num)
    c=len(num)
    return float(s)/c


def cave (di):
    t=list()
    for i in di:
        ca=ave(i['assignment'])
        cl=ave(i['lab'])
        ct=ave(i['test'])
        t.append(ca*0.1+cl*0.2+ct*0.7)
    return ave(t)
            
def gra(gr):
    if gr>=90:
        return "A"
    elif gr>=80:
        return "b"
    elif gr>=70:
        return "c"
    else:
        return "d"

l=[jack,james,dylan,jess,tom]
c=0


for i in l:
    
    average=ave(i["assignment"])
    labb=ave(i["lab"])
    tes=ave(i['test'])
    totaav=(average*0.1)+(labb*0.2)+(tes*0.7)
    print('\n')
    print(i['name'])
    print(totaav)
    print(gra(int(totaav)))
    print('\n')
   

print('cav',cave(l))
print('grade',gra(cave(l)))