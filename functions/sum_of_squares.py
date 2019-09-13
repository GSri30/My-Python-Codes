# Write a function sum_of_squares(a,b,c) which returns a*a+b*b+c*c. Use square(x) to achieve this result.

def sum_of_squares(a,b,c):
    return square(a)+square(b)+square(c)

def square(x):
    count=0
    for i in range(x):
        count+=x
    return count


print(sum_of_squares(input(),input(),input()))
