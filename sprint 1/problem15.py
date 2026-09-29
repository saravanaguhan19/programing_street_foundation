n=int(input())

def print_factor(n):
  small=[]
  large=[]
  i=1
  while i*i <= n:
    if(n%i ==0):
      small.append(i)
      if(i != n // i):
        large.append(n//i)
    i=i+1

  for i in small:
    print(i,end=" ")

  for i in large[::-1]:
    print(i,end=" ")


print_factor(n)