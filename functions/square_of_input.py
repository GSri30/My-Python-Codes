# Write a function square(x) which returns x*x . Use addition to achieve this result

def square(x,i):
    if(i == 1):
        return x
    return x + square(x,i-1)
x = input()
print(square(x,x))
#just used recursions
