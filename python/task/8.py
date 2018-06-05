import turtle

def draw_table(row, bob,column):
    bob.speed(0)
    for i in range(row):
        for j in range(column):
            square(bob)
            bob.fd(100)
        bob.lt(180)
        bob.fd(400)
        bob.lt(90) 
        if(i != row - 1):
            bob.fd(100)
            bob.lt(90)

def square(bob):
    bob.speed(0)
    for i in range(4):
        bob.fd(100)
        bob.lt(90)
bob = turtle.Turtle()
draw_table(3, bob,4)
turtle.mainloop()
