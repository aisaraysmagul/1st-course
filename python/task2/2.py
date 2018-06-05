def letter_grade(n):
    if n>100 or n<0:
        print('invalid grade')
    if 95<=n<=100:
        print('A')
    if  90<=n<=94:
        print('A-')
    if 85<=n<=89:
        print('B+')
    if 80<=n<=84:
        print('B')
    if 75<=n<=79:
        print('B-')
    if 70<=n<=74:
        print('C+')
    if 65<=n<=69:
        print('C')
    if 60<=n<=64:
        print('C-')
    if 55<=n<=59:
        print('D')
    if 50<=n<=54:
        print('D')
    if 0<=n<=49:
        print('F')
letter_grade(49)
letter_grade(75)
letter_grade(101)
