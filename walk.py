import turtle
from turtle import Turtle, Screen
import random

tammy = Turtle()
turtle.colormode(255)


def coloring():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


# colors = ["Black", "Red", "Gold", "Green", "Orange", "Pink", "Brown", "Blue"]
direction = [0, 90, 180, 270]

for _ in range(100):
    tammy.color(coloring())
    tammy.speed(10)
    tammy.pensize(10)
    tammy.forward(30)
    tammy.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()
