def most_used(s):
    t=[]
    for i in s:
        c=s.count(i)
        t.append(c)  
    x=max(t)
    for i in s:
        if s.count(i)==x:
            return i
print(most_used('AAAAaaa'))

