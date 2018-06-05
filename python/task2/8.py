def recurse(n, s):
    if n == 0:            """create a conditional statements"""
        print(s)          """if condition is performed we will print s"""
    else:
        recurse(n-1, n+s) """if condition isn't performed we will use recursion"""
recurse(-1, 0)            
