import turtle
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
    i=0
    p=['red','yellow','green']
    for i in range(3):
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
        t.fillcolor(p[i])
        i=i+1
        t.circle(l.radius)
        t.end_fill()
        b.width=b.width+100
draw_traffic_lights(t,TrafficLights.corner,TrafficLights.box,TrafficLights.lights)
