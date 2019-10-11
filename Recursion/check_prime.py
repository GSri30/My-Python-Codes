#check whether a number is prime or not using recursion

def check_prime(n,i):
    if i==1:
        return 1
    else:
        if n%i==0:
            return 0
        else:
            return check_prime(n,i-1)


