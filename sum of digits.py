#sum of digits
n=int(input())#1234
sum=0
while n>0:
    rem=n%10#4
    qu=n//10#123
    n=qu
    sum+=rem
print(sum)
