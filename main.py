def is_leap(year):
  """ Takes an year and returs if the year is leap year or not """
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return False
      else:
        return True
    else:
      return True
  else:
    return False

def days_in_month(year,month):
    """Takes an year and a month and returns the number of days for that month and year"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2:
        leap_year = is_leap(year)
        if leap_year:
            return 29
        else:
            return 28
    else:
        return month_days[month-1]
    
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












