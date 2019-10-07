# Finding the minimum number of notes required for given amount
# Consider a currency system in which there are notes of seven denominations, namely Rs 1, Rs2, Rs 5, Rs 10, Rs 50 and Rs 200.  If an amount Rs N is entered through the keyboard, write aprogram to compute the smallest number of notes that will combine to give Rs N.

import math
print("Enter the amount in RS: ")
n=int(input())
while n>=200:
    global a
    a=math.trunc(n/200)
    n=n%200
    break
else:
    a=0
while n>=50:
    global b
    b=math.trunc(n/50)
    n=n%50
    break
else:
    b=0
while n>=10:
    global c
    c=math.trunc(n/10)
    n=n%10
    break
else:
    c=0
while n>=5:
    global d
    d=math.trunc(n/5)
    n=n%5
    break
else:
    d=0
while n>=2:
    global e
    e=math.trunc(n/2)
    n=n%2
    break
else:
    e=0
while n>=1:
    global f
    f=n
    break
else:
    f=0
print("The smallest number of notes that combine to give the amount is: ",a+b+c+d+e+f)

