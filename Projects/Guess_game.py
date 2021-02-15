from numpy.core.defchararray import split
from numpy.lib.histograms import histogram_bin_edges


wf=open('/home/ganesh/Documents/Projects/words.txt')
ws=wf.read()
ws=ws.rstrip()
wl=ws.split()
wl1=wl

def limit_counter(c,l,a,le,wl):
    if c<l:
        limit=l-c
        print("\tNow you have ",'\"',limit,'\"','chances\n')
        return letter_input(a,c,le,wl)
    else:
        print('\tyou have ran out of times\n')
        uw=input("\t\t\tEnter the word\n\n")
        if uw.lower()==a.lower():
            print('\t\t\tYOU WON\t\t\n\n','\t\t\tThe word is \"{0}\"'.format(a))
        else:
            print('\t\t\tYOU LOSE\t\t\n\n','\t\t\tThe word is \"{0}\"'.format(a))
    

def letter_check(a,b,c,le,wl):
    al=a.lower()
    cc=0
    for i in al:
          if i==b:
              c+=1 
              cc+=1
    if cc>0:
        print("\tyou entered letter is there in the word for \"{0}\" times\n" .format(cc))
        return limit_counter(c,len(a)-1,a,le,wl)
    else:
        print('\tYou entered letter is not there in the word\n')
        return limit_counter(c+1,len(a)-1,a,le,wl)
    
def hint(wc,wl,c,le):
       hintt=open('/home/ganesh/Documents/Projects/hint.txt')
       ttt=hintt.read() 
       tq=ttt.split(';')
       q=wl1.index(wc)
       print(tq[q])
       ans=input('\t\nIf you get it then type the word\t\n')
       if ans.lower()==wc.lower():
            print('\t\t\tYOU WON\t\t\n\n','\t\t\tThe word is \"{0}\"'.format(wc))
       else:
            print('\t\t\tWrong Go head\t\t\n\n')
            return letter_input(wc,c,le,wl)
          
def letter_input(wc,c,le,wl):
    print("\t\nIf you want to get hint  type hint\n")
    li=input('\tEnter the letter you guess\n')
    if len(li)==1:
            print("\tYou entered letter is \"{0}\"\n".format(li))
            if li in le:
                print("\n\tOOPS You alreay entered this letter\n")
                return letter_input(wc,c,le,wl)
            else:
                le.append(li)
                return letter_check(wc,li,c,le,wl)
    elif li=='hint':
                hint(wc,wl,c,le)
    else:
        print("\n\tOOPS! Enter single letter only\n ")
        return letter_input(wc,c,le,wl)

def word_choose(wl):
    import numpy as np
    wl=np.array(wl)
    wc=np.random.choice(wl)
    le=list()
    print('\tYour word contains ','\"',len(wc),'\'','letters\n')
    print('\tAnd you have ','\"',len(wc)-1,'\"','limits\n')
    print("\tYour letter contains",'\"',len(wc),'\"','words\n')
    return letter_input(wc,0,le,wl)

print('\n \t\t\tLet\'s Play The Game\n\t\t\t')
word_choose(wl)