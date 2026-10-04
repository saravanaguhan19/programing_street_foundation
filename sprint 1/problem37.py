
s = input()

normalized_s=[]

for char in s:
  if char.isalpha():
    cleaned_char=char.lower()
    normalized_s.append(cleaned_char)

i =0
j = len(normalized_s)-1
is_palindrome = True
while i < j :
  if(normalized_s[i] != normalized_s[j] ):
      is_palindrome = False
      break
  i+=1
  j-=1

print("True" if is_palindrome else "False")