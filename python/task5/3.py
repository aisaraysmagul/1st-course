def list_sum(t):
    s=0
    for i in t:
        s=i+s
    print(s)


def nested_sum(t):
    s1=0
    s2=0
    for i in t:
        if type(i)==int:
            s1=s1+i
        else:
            for g in i:
                s2=s2+g
    print(s1+s2)

