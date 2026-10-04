s1=input()
s2=input()

# sorted_s1="".join(sorted(s1))
# sorted_s2="".join(sorted(s2))

# print("Anagram" if sorted_s1 == sorted_s2 else "Not Anagram")



if(len(s1) != len(s2)):
    print("Not Anagram")
else:
    count=[0]*26

    for ch in s1:
        index=ord(ch)-ord('a')
        count[index] += 1
    
    for ch in s2:
        index=ord(ch)-ord('a')
        count[index] -= 1

    if(all(x==0 for x in count)):
        print("Anagram")
    else:
        print("Not Anagram")
    


