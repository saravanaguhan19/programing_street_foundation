s =input()

print("Built-in:",s[::-1])

new_s="";

for char in s:
  new_s = char + new_s

print("Manual:",new_s)