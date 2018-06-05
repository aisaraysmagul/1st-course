def mixed_sum(t):
    a=0
    for i in t:
        if type(i)==list:
            a=a+mixed_sum(i)
        else:
            a=a+i
    return a
    

