n=int(input())

sum=0
i=1
while i*i <=n:
  if(n%i == 0):
    sum = sum +i
  
  i=i+1
 
if(n == sum):
  print("Perfect")
else:
  print("Not Perfect")