dictionary = {0:0, 1:1}
import time
x=time.time()
def fib1(n):
    a=time.clock()
    if n in dictionary:
        return dictionary[n]
    res = fib1(n-1) + fib1(n-2)
    dictionary[n] = res
    return a
def fib2(n):
    b=time.clock()
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)
    ret
def diff(n):
    fib1(n)
    fib2(n)
    print(a,b)
    

