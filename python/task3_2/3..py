def first(x):
    return x[0]
def last(x):
    return x[-1]
def middle(x):
    return x[1:-1]
def is_palindrome(y):
    a=first(y)
    b=last(y)
    if a==b and len(y)==2:
        print('true')
    elif a==b:
        is_palindrome(middle(y))
    else:
        print('false')
is_palindrome('rediveder')
