class Point:
    def __init__(self,a=0,b=0):
        self.x=a
        self.y=b
    def __str__(self):
        return '(%d,%d)'% (self.x,self.y)
    def distance(self,other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**(1/2)
    def __add__(self,other):
        return self.x+other.x,self.y+other.y

p=Point(3,7)
print(p)
class Circle:
    ''' '''
c=Circle()
c.radius=10
c.center=p
#print(c.center);
p2=Point(5,9)
#print(p.distance(p2))
p3=p+p2
#print(p3)
import copy
c2=copy.copy(c)
c2.center.x=4
c2.center.y=10
c.radius=15
print(c.radius,c2.radius)
