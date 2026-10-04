n=int(input())

n_in=n
def digit_sum(n):
  sum=0
  while n > 0:
    sum += n % 10
    n=n//10
  
  return sum


while n_in>=10 :
  n_in=digit_sum(n_in)



if(n==0):
  formula_ans=0
else:
  formula_ans= 1 + ((n-1) % 9)


print("Loop:",n_in)

print("Formula",formula_ans)
