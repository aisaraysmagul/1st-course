def l(a):
    if a%400==0 or (a%4==0 and a%100!=0):
        print(a,'is a leap year')
    else:
        print(a,'is NOT a leap year')
    
l(2016)
l(1999)
l(1800)
