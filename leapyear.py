#This code checks if a year is a leap year or not
def isLeapYear(year):
  if (year%100!=0 and year%4==0) or(year%100==0 and year%400==0):
    return True
  else:
    return False


test_year=int(input())
if(isLeapYear(test_year)):
  print("Leap Year")
else:
  print("Not a leap year")
