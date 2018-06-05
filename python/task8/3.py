import random
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
def choise_from_hist(t):
    hist=histogram(t)
    a=list(t)
    count=sum(hist.values())
    b=random.choice(a)
    print('Probability of',b,'=',hist[b],'/',count)
t='aaaaabbc'
choise_from_hist(t)
