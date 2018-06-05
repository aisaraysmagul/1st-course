def is_triangle(x,y,z):
    if (x+y)<z or (x+z)<y or (y+z)<x:
        print('No')
    elif (x+y)==z or (x+z)==y or (y+z)==x:
        print('"Degenerate" triangle')
    else:
        print('Yes')
is_triangle(1,1,3)
is_triangle(2,1,3)
is_triangle(5,3,3)
    
