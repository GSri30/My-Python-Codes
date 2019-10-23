#Write a recursive function sumDigits(n) to calculate the sum of all the digits of n

def sumDigits(n):
## Your code - begin

    #store the number of digits in a variable
    num_digits=len(str(n))
    #if number has only one digit, return the same number
    if num_digits==1:
        return n
    #else return sum of digits except first digit and add that first digit to sum obtained
    return (n/(10**(num_digits-1)))+sumDigits(n%(10**(num_digits-1)))

## Your code - end

