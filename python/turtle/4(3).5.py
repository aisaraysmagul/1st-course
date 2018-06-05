def polygon(n):
    import turtle
    bob=turtle.Turtle()
    print(bob)  
    for i in range (n):
        bob.fd(15)
        bob.lt(360/n)
def circle(n):
    polygon(n)
    

def arc(angle):
    circle(angle)
arc(360)
