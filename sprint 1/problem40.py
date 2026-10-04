mode = input().strip()
k= int(input())
text=input()


shift= k % 26
if(mode == 'DECODE'):
    shift = (26-shift) % 26

out=[]

for ch in text:
    if( 'A' <= ch <= 'Z'):
        out.append(chr((ord(ch)-ord("A")+shift )% 26 +ord("A")))
    elif('a' <= ch <= 'z'):
        out.append(chr((ord(ch)-ord("a")+shift)% 26 + ord("a")))
    else:
        out.append(ch) #non letter unchanged

print("".join(out));

#problem 40 doubt dont understand this logic