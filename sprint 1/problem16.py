b=int(input())
e=int(input())


def iterative_pow(b,e):
  iterative=1

  while e!=0:
    iterative*=b
    e-=1
  return iterative

def recursive_pow(b,e):
  if(e == 0):
    return 1
  return b * recursive_pow(b,e-1)

print("Iterative:",iterative_pow(b,e))
print("Recursive:",recursive_pow(b,e))