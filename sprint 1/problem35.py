s =input()

vowels=0
consonants=0
for char in s:
  if(char == " "):
    continue
  if(char == 'a' or char == 'e' or char == 'i' or  char == 'o' or char == 'u' ):
    vowels +=1
  else:
    consonants +=1

print(f"Vowels={vowels}, Consonants={consonants}")