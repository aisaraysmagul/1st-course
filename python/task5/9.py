import random
def birthday_paradox(n):
    t = []
    s=[]
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)
    for j in t:
        c=t.count(j)
        s.append(c)
    for g in s:
        if g>1:
            return True
    return False
def birthday(x):
    a=0
    for i in range(x):
        if birthday_paradox(23) is True:
            a=a+1
    percent=int((a/x)*100)
    print('Percent of True is',percent,'%')
