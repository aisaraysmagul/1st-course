import turtle
import copy
class Point:
    def __init__(self,a=0,b=0):
        self.x=a
        self.y=b

class Rectangle:
    def __init__(self,a=100,b=100):
        self.width=a
        self.height=b
        self.corner=Point()

class Circle:
    def __init__(self,a=50):
        self.radius=a
        self.center=Point()

class TrafficLights:
    corner=Point()
    box=Rectangle()
    lights=Circle()

t=turtle.Turtle()
def draw_traffic_lights(t,c,b,l):
    t.pu()
    t.setposition(c.x,c.y)
    t.pd()
    for i in range(2):
        t.fd(b.height)
        t.lt(90)
        t.fd(b.width)
        t.lt(90)
    t.pu()
    t.setposition(c.x+(b.height/2),c.y)
    t.pd()
    t.begin_fill()
    t.fillcolor('red')
    t.circle(l.radius)
    t.end_fill()
    t.pu()
    t.setposition(c.x,c.y)
    t.pd()
    for i in range(2):
        t.fd(b.height)
        t.rt(90)
        t.fd(b.width)
        t.rt(90)
    t.pu()
    t.setposition(c.x+(b.height/2),c.y-b.width)
    t.pd()
    t.begin_fill()
    t.fillcolor('yellow')
    t.circle(l.radius)
    t.end_fill()
    t.pu()
    t.setposition(c.x,c.y-b.width)
    t.pd()
    for i in range(2):
        t.fd(b.height)
        t.rt(90)
        t.fd(b.width)
        t.rt(90)
    t.pu()
    t.setposition(c.x+(b.height/2),c.y-(2*b.width))
    t.pd()
    t.begin_fill()
    t.fillcolor('green')
    t.circle(l.radius)
    t.end_fill()
def copying(t):
    light2=copy.copy(TrafficLights)
    t.begin_fill()
    t.fillcolor('black')
    light2.lights.radius=25
    t.circle(light2.lights.radius)
    t.end_fill()
copying(t)
draw_traffic_lights(t,TrafficLights.corner,TrafficLights.box,TrafficLights.lights)
