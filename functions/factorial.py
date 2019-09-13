# Write a function fact(n) which returns the factorial of a number

def fact(n):
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
    return factorial

print(fact(input()))
