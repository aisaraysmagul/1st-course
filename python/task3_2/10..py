def prime3():
    print(1,end=' ')
    for i in range(2,1001):
        for j in range(2,i):
            if (i%j==0):
                break
        
        else:
            if len(str(i))==1:
                num1=i
                print(num1,end=' ')
            else:
                if len(str(i))==2:
                    num2=i
                    print(num2,end=' ')
                else:
                    len(str(i))==3
                    num3=i
                    print(num3,end=' ')
def is_prime(n):
    for i in range(2,int (n**0.5)+1):
        if n%1==0:
            return False
    return True
def prime():
    for i in range(1000):
        if is_prime(i+1):
            print(i+1)
'''def prime2():
    for i in range(1,10):
        if is_prime(i):
            print(i,end=' ')
    print('\n')
    for i in range(10,100):
        if is_prime(i):
            print(i,end=' ')
    print('\n')
    for i in range(100,1000):
        if is_prime(i):
            print(i,end=' ')
prime2()'''
prime()

