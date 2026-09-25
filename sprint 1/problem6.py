n = int(input())

import math
def is_prime(n):

  if(n <= 1): return False

  if (n==2): return True

  if(n%2==0): return False

  for i in range(3,int(math.sqrt(n)),2):
    
    if(n%i == 0): return False

  return True 


if is_prime(n):
  print("Prime")
else:
  print("Not prime")
    
    