
n=int(input())

import math 

if(n<2):
  print("Not a prime")
else:
  for i in range(2,int(math.sqrt(n))):
    