n=int(input())

factorial=1

for i in range(1,n+1):
    factorial*=i

print(f"{n}! = ",factorial)


if n<2:
  print(f"Smallest factor > 1 : none")

else:
  i=2
  while i <n:
    if(n%i ==0):
      break
    i+=1
  if(n==i):
    print(f"Smallest factor > 1 : {i} (Prime)")
  else:
    print(f"Smallest factor > 1 : {i} (Not Prime)")



  