import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)


def coloring():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


for x in range(100):
    tim.color(coloring())
    tim.speed(0)
    tim.circle(100)
    tim.tiltangle(45)
    tim.right(25)

screen = Screen()
screen.exitonclick()