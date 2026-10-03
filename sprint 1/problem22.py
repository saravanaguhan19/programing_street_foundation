t_str,scale = input().split()
t=float(t_str)

if(scale == 'C'):
  c=t
elif(scale == 'F'):
  c = (t- 32)*(5/9)
else:
  c=t-273.15


f= (c*(9/5)) +32

k =c +273.15

if(scale == 'C'):
  print(f"F={f:.2f},K={k:.2f}")
elif(scale == 'F'):
  print(f"C={c:.2f},K={k:.2f}")
else:
  print(f"C={c:.2f},F={f:.2f}")

