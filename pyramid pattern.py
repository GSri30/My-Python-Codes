n=int(input())
for i in range(0,n):

    for j in range(0,n-i):
        print(end=' ')

    for j in range(i+1):
        print('* ',end=' ')
    i+=1
    print()
