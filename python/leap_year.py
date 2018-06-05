def is_year_leap(x):
    if x%4==0 and (x%400==0 or x%100!=0):
        return True
    else:
        return False
