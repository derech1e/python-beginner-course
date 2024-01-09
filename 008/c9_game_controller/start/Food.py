from random import randint
import turtle


class Food:

    def __init__(self):
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape("square")
        self.food.color('red')
        self.food.penup()
        self.find_new_location()  # Mit dem Initialisieren der Klasse wird eine zufällige Position gewählt

    def find_new_location(self):
        # Diese Funktion kann noch weitere optimiert werden, da sie momentan von statischen werten abhängig ist
        x = randint(-290, 290)
        y = randint(-290, 290)
        self.food.goto(x, y)
