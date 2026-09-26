n=int(input())

def fibonacci_series(n):
  if(n==1):
    print(0,end=" ")
    return
  if(n==2):
    print(0,1, end=" ")
    return   
  a=0 
  b=1
  print(a,b,end=" ")
  for i in range(3,n+1):
    temp=a+b
    print(temp,end=" ")
    a=b
    b=temp
  
fibonacci_series(n) 