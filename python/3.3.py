def do_twice(f):
        f()
        f()

def do_four(f):
        do_twice(f)
        do_twice(f)

def print_line():
        print("+ - - - -", end= ' ')
def print_line2():
        print("|        ", end=' ')

def print_3():
        print_1()
        do_four(print_2)
def print_1():
        do_twice(print_line)
        print("+")
def print_2():
        do_twice(print_line2)
        print("|")
def print_grid():
        do_twice(print_3)
        print_1()

print_grid()
