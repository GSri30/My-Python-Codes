import math

n=int(input())
sum=0
while n>0:
    unit=n%10
    sum += unit
    n = math.floor(n/10)
print(sum)
