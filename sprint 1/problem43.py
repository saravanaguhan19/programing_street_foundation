n=int(input())

arr=list(map(int,input().split()))

max=arr[0]
min=arr[0]
total=0
for x in arr:
  if(x> max):
    max=x
  if(x < min):
    min=x
  
  total +=x

print(f"Max={max},Min={min},Sum={total},Avg={total/n:.2f}")