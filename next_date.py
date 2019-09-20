#find the next date of the input date

day=int(input())
month=int(input())
year=int(input())

def is_leap_year(month):
  if (year % 4) == 0:
    if (year % 100) == 0:
      if (year % 400) == 0:
        return 1
      else:
        return 0
    else:
      return 1
  else:
    return 0

if month in (1,3,5,7,8,10,12):
  month_length=31
elif month==2:
  if is_leap_year(month):
    month_length=29
  else:
    month_length=28
else:
  month_length=30
  

def triple(day,month,year):
  i=1
  if day<month_length and month<13:
    day+=1
  elif day==month_length:
    day=1
    if month==12:
      month=1
      year+=1
    else:
      month+=1
  else:
    i=0
    print("inval")
  if i!=0:
    print(day, end=' ')
    print(month, end=' ')
    print(year)

triple(day,month,year)








