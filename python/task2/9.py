import turtle
def draw(t, l, n):
    if n == 0:
        return
    angle = 50
    t.fd(l*n)
    t.lt(angle)
    draw(t, l, n-1)    
    t.rt(2*angle)
    draw(t, l, n-1)
    t.lt(angle)
    t.bk(l*n)
t=turtle.Turtle()
draw(t,10,4)
