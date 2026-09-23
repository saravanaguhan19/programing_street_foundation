
A=5
B=10

print("Sum=",A+B ,", ","Diff=",A-B,", ","Product=",A*B,", ","Quotient=",A//B)

temp = A 
A=B
B=temp

print("Swap with temp: ","A=",A,"B=",B) 

A=A+B
B=A-B
A=A-B

print("Swap without temp: ","A=",A,"B=",B) 
