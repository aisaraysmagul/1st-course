def check_fermat(a,b,c,n):
    if n>2 :
        print('No,does not work')
    elif (n>2) and (a**n)+(b**n)==(c**n):
        print('Holy smokes, Fermat was wrong!')
    else:
        print('You should write n>2')
check_fermat(5,4,2,5)
def prompt():
    x='Please,enter value of a = '
    a=int(input(x))
    y='Please,enter value of b = '
    b=int(input(y))
    z='Please,enter value of c = '
    c=int(input(z))
    p='Please,enter value of n = '
    n=int(input(p))
    check_fermat(a,b,c,n)
    
prompt()
