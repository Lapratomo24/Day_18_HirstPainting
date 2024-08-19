from turtle import Turtle, Screen

timmy = Turtle()
for x in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
    timmy.color("red")

screen = Screen()
screen.exitonclick()
