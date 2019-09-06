#write a function to print N terms of the fibonacci sequence

def fibonacci(n):
    a=1
    print(a)
    b=1
    print(b)
    for i in range(n-2):
        c=a+b
        a=b
        b=c
        print(c)

fibonacci(5)

