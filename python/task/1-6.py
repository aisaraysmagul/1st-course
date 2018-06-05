def sec_to_time(sec):
    hour=sec//3600
    minute=sec%3600//60
    second=sec%60
    print(hour,':',minute,':',second)
sec_to_time(4000)


def distance (x1,y1,x2,y2):
    res=(((x2-x1)**2)+(y2-y1)**2)**(1/2)
    print('distance between two points=',res)
distance(0,1,3,5)

def cylinder_volume(r,h):
    import math
    v = math.pi*(r**2)*h
    return int(v)


print(cylinder_volume(4,10))
    
def center(a):
    z=len(a)
    d=' '
    c=35-int(z/2)
    r=c*d+a
    print(r)
center('word')
center('satisfactory')
center('multipe word phrase')


def sum(n):
    a=0
    for i in range(n):
        a=(i+1)+a
    print(a)
sum(5)


def factorial(a):
    s=1
    for i in range(a):
        s=s*(i+1)
    print(s)
factorial(4)
