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


def draw_circle(stopgap):
    for x in range(int(360 / stopgap)):
        tim.color(coloring())
        tim.speed(0)
        tim.circle(100)
        tim.setheading(tim.heading() + stopgap)


draw_circle(10)

screen = Screen()
screen.exitonclick()