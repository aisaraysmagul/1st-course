import turtle
import math
def draw_s(t,r):
    t.rt(90)
    c=math.pi*r
    l=c/50
    for i in range(50):
        t.fd(l)
        t.lt(270/50)
    for j in range(50):
        t.fd(l)
        t.rt(270/50)
def draw_d(t,rad):
    t.up()
    t.lt(90)
    t.fd(25)
    t.lt(90)
    t.fd(25)
    t.lt(180)
    t.down()
    t.fd(125)
    t.lt(90)
    a=math.pi*rad
    le=a/63
    for z in range(63):
        t.fd(le)
        t.lt(185/63)

def draw_u(t):
    t.lt(180)
    t.up()
    t.fd(89)
    t.rt(95)
    t.down()
    t.fd(125)
    t.lt(90)
    t.fd(60)
    t.lt(90)
    t.fd(125)
def draw_word(n):
    draw_s(t,50)
    draw_d(t,64.5)
    draw_u(t)
t=turtle.Turtle()
draw_word('sdu')
turtle.mainloop()
