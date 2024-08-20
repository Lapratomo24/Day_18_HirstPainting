from turtle import Turtle, Screen
import colorgram, random

colors = colorgram.extract("hirst.jpg", 20)
list_of_colors = []


def list_colors():
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        list_of_colors.append((r, g, b))


list_colors()
print(list_of_colors)

screen = Screen()
screen.exitonclick()
