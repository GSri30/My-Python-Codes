# pascal triangle
# Write a function which returns the nth row of pascal triangle

def fact(num):
    factorial=1
    for i in range(1,num+1):
        factorial=factorial*i
    return factorial

def binomial(n, r):
    return (fact(n))/(fact(n-r)*fact(r))
def pascal(z):
    for i in range(z):
        print("\b"+str(binomial(z-1, i))),


pascal(input())
