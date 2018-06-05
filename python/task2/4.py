def sum_of_digit(n):
    a = str(n)
    sum = 0
    for i in range(len(a)):
        sum =sum + (n%10)
        n=n//10
    print (sum)
sum_of_digit(123)
sum_of_digit(22222)

def sum2(x):
    if x==0:
        return x%10
    res= x%10+sum2(x//10)
    return res
sum2(1234)
