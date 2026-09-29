n=int(input())

sum=0
i=1
while i*i <=n:
  if(n%i == 0):
    sum = sum +i
    if(i != n // i):  #to avoid square remove the duplicate 
      sum += n //i
  i=i+1

sum =sum -n
 
if(n == sum):
  print("Perfect")
else:
  print("Not Perfect")