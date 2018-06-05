class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y

p=Point(3,4)
vars(p)
def print_attributes(obj):
    for attr in vars(obj):
        print(attr,getattr(obj,attr))

p2=Point()
