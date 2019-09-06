#Write a function to check whether a number is an Armstrong number. An Armstrong number is a number where the sum of it's digits each raised to the power of the number of digits equals the given number. For e.g.:371 is an Armstrong number: 3^3+7^3+1^3=371


def len_number(n):
    count=0
    while(n>=1):
        count+=1
        n=n/10
    return count

def armstrong(n):
    summ=0
    num=len_number(n)
    while(n>0):
        unit=n%10
        summ+=pow(unit, num)
        n=abs(n/10)
    return(summ)

number=input()
if armstrong(number)==number:
    print('T')
else:
    print('F')



    

