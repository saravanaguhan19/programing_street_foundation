a = int(input())
b = int(input())

import math
def is_prime(n):

  if(n < 2): 
    return False
  i=2
  while i*i <=n:
    if n % i ==0:
      return False
    i+=1
  return True 

prime=[]
for i in range(a,b+1):
  if(is_prime(i)):
    # print(i,end=" ")
    prime.append(str(i))  

if(len(prime) ==0):
  print("None")
else:
  print(" ".join(prime))