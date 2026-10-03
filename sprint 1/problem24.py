a,c,d = map(int,input().split())


# if(a >= 18 and c == 1 and d ==0):
#   print("Eligible")
# else:
#   print("Not Eligible -",end=" ")

#   if(a < 18):
#     print("Too Young ,",end=" ")
#   if(c != 1):
#     print("Not a citizen,",end=" ")
#   if(d != 0):
#     print("Disqualified")

  
reasons=[]

if(a < 18):
  reasons.append("Too young")
if(c != 1):
  reasons.append("Not a citizen")
if(d != 0):
  reasons.append("Disqualified")


if reasons:
  print("Not Eligible - " + ", ".join(reasons))
else:
  print("Eligible")