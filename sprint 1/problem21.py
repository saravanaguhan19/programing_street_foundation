

a_str,op,b_str=input().split()
a=int(a_str)
b=int(b_str)

match op:
  case '+':
    print(a+b)
  case '-':
    print(a-b)
  case '*':
    print(a*b)
  case '/':
    if(b==0):
      print("Error:Division by zero")
    else:
      print(f"{a/b:.2f}")
  case '%':
    if(b==0):
      print("Error: Division by zero")
    else:
      print(a%b)
  case _:
    print("Invalid operator")