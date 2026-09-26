n=int(input())

def reversedNumber(n):
  reverseNumber=0

  while n>0:
      digit= n%10
      reverseNumber = (reverseNumber*10) + digit
      n=n//10

  return reverseNumber

if n == reversedNumber(n):
  print("Palindrome")
else:
  print("Not Palindrome")
    