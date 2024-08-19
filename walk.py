from turtle import Turtle, Screen
import random

tammy = Turtle()

colors = ["Black", "Red", "Gold", "Green", "Orange", "Pink", "Brown", "Blue"]
direction = [0, 90, 180, 270]


for _ in range(100):
    tammy.color(random.choice(colors))
    tammy.speed(10)
    tammy.pensize(10)
    tammy.forward(30)
    tammy.setheading(random.choice(direction))


screen = Screen()
screen.exitonclick()