import turtle

screen = turtle.Screen()
screen.setup(width=700, height=700)
t = turtle.Turtle()

# implementation here

screen.listen()  # Setzt den Fokus auf die Turtle um auf Eingaben zu 'hören'
screen.onkeypress(FUNCTION_HERE, KEY_HERE) # Doku hier: https://docs.python.org/3.12/library/turtle.html#turtle.onkeypress

screen.mainloop()


