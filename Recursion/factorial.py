#Write a recursive solution to calculate the factorial of a number.

def factorial(n):
## Your code - begin

    #if n is less than one,return one
    if n<1:
        return 1
    #else calculate n-1 factorial and multiply with n
    return n*factorial(n-1)


## Your code - end

