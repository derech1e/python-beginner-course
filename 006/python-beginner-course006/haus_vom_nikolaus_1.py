import turtle
import math

screen = turtle.Screen()
t = turtle.Turtle()
length = 100

t.fd(length)
t.lt(135)
t.fd(math.sqrt(length ** 2 + length ** 2))
t.rt(135)
t.fd(length)
t.lt(135)
t.fd(math.sqrt(length ** 2 + length ** 2) / 2)
t.lt(90)
t.fd(math.sqrt(length ** 2 + length ** 2) / 2)
t.lt(45)
t.fd(length)
t.lt(135)
t.fd(math.sqrt(length ** 2 + length ** 2))
t.rt(135)
t.fd(length)
# over the street
t.lt(90)
t.fd(length)
# Do it again
t.fd(length)
t.lt(135)
t.fd(math.sqrt(length ** 2 + length ** 2))
t.rt(135)
t.fd(length)
t.lt(135)
t.fd(math.sqrt(length ** 2 + length ** 2) / 2)
t.lt(90)
t.fd(math.sqrt(length ** 2 + length ** 2) / 2)
t.lt(45)
t.fd(length)
t.lt(135)
t.fd(math.sqrt(length ** 2 + length ** 2))
t.rt(135)
t.fd(length)


screen.mainloop()
