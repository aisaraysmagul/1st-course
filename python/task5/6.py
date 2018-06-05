def word_sort():
    x=input('Enter your words separated by comma(no spaces):''\n')
    y=x.split(',')
    y.sort()
    print('Your words sorted out:')
    for i in y:
        if i==y[-1]:
            print(i)
        else:
            print(i, end=',')
word_sort()
