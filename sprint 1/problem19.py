s=int(input())


if(s>=90 and s<= 100):
  grade="A"
elif(s>=75 and s<= 89):
  grade="B"
elif(s>=60 and s<=74):
  grade="C"
elif(s>=50 and s<=59):
  grade="D"
elif(s>=0 and s<=49):
  grade="F"
else:
  grade="Invalid"


print(grade)