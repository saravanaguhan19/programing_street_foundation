n=int(input())

arr = list(map(int,input().split()))

largest=arr[0]
second_largest=None
smallest=arr[0]
second_smallest=None

for val in arr:
  if(val > largest):
    second_largest = largest
    largest=val
  elif(val != largest and (second_largest is None or val > second_largest)):
    second_largest =val    
  if(val < smallest):
    second_smallest=smallest
    smallest=val
  elif(val != smallest and (second_smallest is None or val < second_smallest)):
    second_smallest = val

    

print(f"2nd Largest={second_largest},2nd Smallest={second_smallest}")