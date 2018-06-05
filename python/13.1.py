import string
def chapter13_1(x):
    y=open(x)
    a=[]
    c=[]
    for line in y:
        a.append(line.strip())
        for i in a:
            b=i.split()
        for j in b:
            d=j.split('.')
            for p in d:
                r=p.split(',')
            for q in r:
                for k in string.punctuation:
                    if q.lower()!=k and q.lower() not in c:
                        c.append(q.lower())
    for i in c:
        if i!='':
            print(i)
        
chapter13_1('word.txt')
