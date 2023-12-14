import turtle

screen = turtle.Screen()
t = turtle.Turtle()


def baum(h):
    t.rt(180)

    for i in range(h):
        t.fd(5 + (h * 10) / (i + 1))
        t.rt(135)
        t.fd(75)
        t.lt(135)

    for i in range(h):
        t.lt(135)
        t.fd(75)
        t.rt(135)
        t.fd(5 + (h * 10) / (h - i + 1))


baum(5)

screen.mainloop()
