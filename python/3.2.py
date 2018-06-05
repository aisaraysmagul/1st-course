def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')


do_twice(print_spam)

def do_twice(f,a):
    f(a)
    f(a)

def print_twice(a):
    print(a)
    print(a)

def do_four(f,a):
    do_twice(f,a)
    do_twice(f,a)

do_twice(print_twice,'spam')
print(' ')
do_four(print_twice,'spam')
