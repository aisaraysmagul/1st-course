class Point:
    def __init__(self,a=0,b=0,c=0):
        self.x=a
        self.y=b
        self.r=a+b
        self.z=c
        
    def __str__(self):
        return ('(%d,%d)' % (self.x,self.y))
    def distance(self,another):
        return math.sqrt((self.x-another.x)**2+(self.y-another.y)**2)
    def print_point(self):
        print('(%d,%d)'%(self.x,self.y))
    def add(self,other):
        return(self.x+other.x,self.y+other.y)
    def __add__(self,other):
        return(self.x+other.x,self.y+other.y)
    def __lt__(self,other):
        return self.x<other.x and self.y<other.y
p=Point(3,7)
p.print_point()
class Circle:
    '''Circle'''

c=Circle()
c.rad=10
c.center=p
import math
def area(c):
    return c.rad**2*math.pi
p2=Point(5,8)
p2.x=5
p2.y=9
p3=p.add(p2)
print(p3)
print(p<p2)
import turtle
bob=turtle.Turtle()
def draw_circle(bob,c):
    bob.pu()
    bob.setposition(c.center.x,c.center.y)
    bob.pd()
    bob.circle(c.rad)
draw_circle(bob,c)
print(p.z)
