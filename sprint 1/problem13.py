n=int(input())

def isArmstrongNumber(n):
  temp = n
  count=0
  while(temp >0):
    count+=1
    temp=temp//10
  
  createdNumber=0

  temp=n
  while(temp>0):
    tempDigit= temp%10
    createdNumber += tempDigit ** count
    temp=temp//10
  
  if(n == createdNumber):
    print("Armstrong")
  else:
    print("Not Armstrong")
  
  
isArmstrongNumber(n)


