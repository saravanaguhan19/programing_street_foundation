n=int(input())
if(n==0):
  count=1
else:
  count=0
sum=0
while(n!=0):
  count+=1
  last_digit=n%10
  print(last_digit)
  sum+=last_digit
  print(sum)
  n=n//10

print(f"Count={count}, Sum={sum}")