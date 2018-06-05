#a
def is_even(n):
    if n%2==0:
        n=True
        print (n)
    else:
        
        n=False
        print(n)
    return(n)
#b
def is_even1(n):
    if n%2==0:
        n=True
    else:
        n=False
    return(n)


def all_even(n):
    for i in range(n+1):
        if is_even1(i):
            print(i)
is_even(5)
is_even(8)
all_even(12)
all_even(9)

