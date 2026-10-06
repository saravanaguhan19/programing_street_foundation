n=int(input())

arr = list(map(int,input().split()))

i=0
j=n-1

while i < j:
  temp = arr[i]
  arr[i]=arr[j]
  arr[j]=temp

  # arr[i] , arr[j] = arr[j] , arr[i]
  i=i+1
  j=j-1


print(arr)