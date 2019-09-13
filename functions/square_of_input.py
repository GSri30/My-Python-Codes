# Write a function square(x) which returns x*x . Use addition to achieve this result

def square(x):
    count=0
    for i in range(x):
        count+=x
    return count

print(square(input()))

