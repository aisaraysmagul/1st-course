import math
class Shape(object):
    def __str__(self):
        return 'Shape object'
    def area(self):
        return None
class Circle(Shape):
    def __init__(self,r):
        self.radius=r
    def area(self):
        return math.pi*self.radius**2
class Rectangle(Shape):
    def __init__(self,w,h):
        self.width=w
        self.height=h
    def area(self):
        return self.width*self.height
class Square(Rectangle):
    def __init__(self,a):
        super().__init__(a,a)
    def __str__(self):
        return 'Square object'
sh=Shape()
print(sh)
print(sh.area())
c=Circle(10)
print(c)
print(c.area())
r=Rectangle(20,5)
print(r.area())
s=Square(3)
print(s)
print(s.area())
