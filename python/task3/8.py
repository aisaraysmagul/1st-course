#a
"""a=input('Enter your PIN number: ')
while a!='1234':
    a=input('Error! Enter again: ')
print('Correct!')"""
#b
a=input('Enter your PIN number: ')
if a=='1234':
    print('Correct!')
else:
    for i in range(2):
        a=input('Error! Enter again: ')
        if a=='1234':
            break
    if a!='1234':
        print('Error! Your card has been blocked.')
    else:
        print('Correct')                                                                                                    
