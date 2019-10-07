# Arithematic operations
# Build  a  calculator  program  that  provides  the  facility  to  do  the  following  simple  arithmetic computations on two numbers: 1.  Add  2.  Multiply  3.  Average.
# Provide a text based menu which provides the above choices as numerical inputs. Once selected,the program accepts the two numbers one by one, and exits after printing out the result basedon the chosen operation.

print("Enter the serial number of required operation: \n1.Add\n2.Multiply\n3.Average\n")
x=input()

if x =='1':
    print("Enter the first number: ")
    a=int(input())
    print("Enter the second number: ")
    b=int(input())
    print("Sum = ",a+b)
elif x=='2':
    print("Enter the first number: ")
    a=int(input())
    print("Enter the second number: ")
    b=int(input())
    print("Product = ",a*b)
elif x=='3':
    print("Enter the first number: ")
    a=int(input())
    print("Enter the second number: ")
    b=int(input())
    print("Average = ",(a+b)/2)
else:
    print()
