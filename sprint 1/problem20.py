a=int(input())
b=int(input())
c=int(input())


def sayTypeTriangle(a,b,c):
  if(a+b > c and b+c > a and a+c > b):
    print("Valid -" , end=" ")
    if(a == b == c):
      print("Equilateral")
    elif(a != b != c):
      print("Scalene")
    else:
      print("Isosceles")

  else:
    print("Not a valid triangle")


sayTypeTriangle(a,b,c)