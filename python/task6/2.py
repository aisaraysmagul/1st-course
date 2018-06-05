def most_used2(s):
    d= dict()
    
    for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    x=max(d.values())
    for i in s:
        if d[i]==x:
            return i
    
