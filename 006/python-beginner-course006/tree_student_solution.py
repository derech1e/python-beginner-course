import turtle

screen = turtle.Screen()
t = turtle.Turtle()


def baum(height, runter, rein):
    t.speed(100)
    t.penup()
    t.goto(0, 300)
    t.pendown()

    for i in range(0, height):
        t.rt(45)
        t.fd(runter)
        t.rt(135)
        t.fd(rein)
        t.rt(180)
    t.penup()
    t.goto(0, 300)
    t.rt(180)
    t.pendown()
    for i in range(0, height):
        t.lt(45)
        t.fd(runter)
        t.lt(135)
        t.fd(rein)
        t.rt(180)


baum(5, 100, 50)
screen.mainloop()
