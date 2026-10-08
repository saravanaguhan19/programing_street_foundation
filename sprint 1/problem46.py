n=int(input())

arr = list(map(int,input().split()))

counts={}

for x in arr:

  if(x in counts):
    counts[x] = counts[x] + 1
  else:
    counts[x]=1


result=[]

for key in counts:
  result.append(str(key)+":"+str(counts[key]))

print(",".join(result))