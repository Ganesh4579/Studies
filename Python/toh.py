def toh(n,s,d,a):
      if n==1:
              print("move rode %d from  %s to  %s " %(n,s,d) )
              return 
      toh(n-1,s,a,d)
      print("move rode %d from %s to %s " %(n,s,d))
      toh(n-1,a,d,s)
n=int(input('e'))
toh(n,'s','d','a')