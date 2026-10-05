s=input()

ans=[]
seen = set()

for ch in s:

  if ch not in seen :
    seen.add(ch)
    ans.append(ch)

print("".join(ans))