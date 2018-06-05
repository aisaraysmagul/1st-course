def has_duplicates(t):
    s=[]
    for i in t:
        c=t.count(i)
        s.append(c)
    for g in s:
        if g>1:
            return True
        else:
            return False

def remove_duplicates(t):
    z = []
    for i in t:
        if i not in z:
            z.append(i)
    return z
