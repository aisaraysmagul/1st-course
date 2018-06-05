def eval_loop():
    x=input('Please, enter something : ')
    while x!='done':
        y=eval(x)
        print(y)
        x=input('Please, enter something : ')
        if x=='done':
            break
    return y
eval_loop()
