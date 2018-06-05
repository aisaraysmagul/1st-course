import random
def game():
    num=random.randint(0,100)
    x=int(input('Guess the number:'))
    count=1
    while x!=num:
        if x>num:
            x=int(input('Your number bigger than mine: '))
            count=count+1
        if x<num:
            x=int(input('Your number less than mine: '))
            count=count+1
    print('You won')
    print('The total number of your guesses =', count)
    
game()
def game2():
    num=random.randint(0,100)
    x=int(input('Guess the number:'))
    count=0
    for i in range(6):
        if x>num:
            x=int(input('Your number bigger than mine: '))
        elif x<num:
            x=int(input('Your number less than mine: '))
        else:
            print('You won')
            break
        if i==5:
            print('Your trials is over,you lose')
            break
game2()
