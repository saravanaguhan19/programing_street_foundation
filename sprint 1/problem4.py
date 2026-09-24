n=int(input())
sum=0

for i in range(1,n+1):
    sum+=i

print("For loop: ",sum)

sum=0

i=0
while i<=n:
  sum+=i
  i+=1

print("While loop: ",sum)

sum=0

sum= int(n*(n+1)/2)

print("Formula: " , sum)