import copy
class Point():
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
    pass
class Rectangle():
    pass
p = Point()
p.x = 10
p.y = 20
r1 = Rectangle()
r1.width = 200
r1.height = 100
r1.corner = p
r2 = r1
r2.width = 300
print(r1 == r2, r1 is r2) 
print(r1.width==r2.width)
r3 = copy.copy(r1)
r3.width = 400
r3.corner.x = 30
print(r1 == r3, r1 is r3) 
print(r1.width==r3.width) 
print(r1.corner.x==r3.corner.x) 
r4 = copy.deepcopy(r1)
r4.width = 500
print(r1 == r4, r1 is r4) 
print(r1.width==r4.width) 
print(r1.corner==r4.corner, r1.corner is r4.corner)
