import turtle
def draw(t, n):
    t.speed(0)
    if n <10:
        t.fd(n)
        return
    m=n/3
    draw(t,m)
    t.lt(60)
    draw(t, m)
    t.rt(120)
    draw(t, m)
    t.lt(60)
    draw(t,m)
t=turtle.Turtle()
draw(t,30)
turtle.mainloop()
