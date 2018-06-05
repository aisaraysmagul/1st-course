def prime(n):
    for i in range(2,n):
        if(n%i==0): return False
    return True
for i in range(1,1000):
    if (prime(i)):
        print(i, end=' ')
        

