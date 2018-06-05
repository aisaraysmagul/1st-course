def is_anagram(x,y):
    a=list(x)
    b=list(y)
    a.sort()
    b.sort()
    if a==b:
        return True
    else:
        return False
