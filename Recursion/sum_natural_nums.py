#find sum of first n natural numbers using recursion

def sum_nums(n):
    if n<1:
        return 0
    return n + sum_nums(n-1)


