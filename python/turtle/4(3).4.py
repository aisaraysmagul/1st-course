def polygon(n,lenght):
    import turtle
    bob=turtle.Turtle()
    print(bob)  
    for i in range (n):
        bob.fd(lenght)
        bob.lt(360/n)
def circle(n,lenght):
    polygon(n,lenght)
    

circle(10,10)    
