y=int(input())


def leap_year_check(y):
  if(y %4==0 and (y%100!=0  or y%400==0)):
    print("Leap year")
  else:
    print("Not a Leap year")


leap_year_check(y)