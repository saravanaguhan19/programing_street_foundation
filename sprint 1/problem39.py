s = input()
word = input()

split_s = s.split()

word=word.lower()

count=0
for w in split_s :
    w=w.lower()
    if(word == w ):
        count += 1


print(count)
