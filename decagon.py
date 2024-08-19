from turtle import Turtle, Screen
import random

tommy = Turtle()

colors = ["Black", "Red", "Gold", "Green", "Orange", "Pink", "Brown", "Blue"]


def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        tommy.forward(100)
        tommy.right(angle)


for x in range(3, 11):
    tommy.color(random.choice(colors))
    draw_shape(x)

screen = Screen()
screen.exitonclick()

