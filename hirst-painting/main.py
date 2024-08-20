from turtle import Turtle, Screen
import colorgram, random, turtle

# colors = colorgram.extract("hirst.jpg", 20)
# list_of_colors = []


# def list_colors():
#    for color in colors:
#        r = color.rgb.r
#        g = color.rgb.g
#        b = color.rgb.b
#        list_of_colors.append((r, g, b))


# list_colors()
# print(list_of_colors)

hirst_colors = [(246, 246, 241), (29, 101, 154), (181, 63, 28), (249, 168, 83),
                (186, 45, 111), (218, 211, 62), (242, 210, 215), (233, 244, 238),
                (243, 154, 185), (122, 205, 188), (146, 196, 3), (175, 120, 155),
                (170, 204, 191), (4, 127, 70), (252, 95, 6), (236, 243, 249),
                (253, 196, 0), (205, 16, 94), (2, 121, 66), (169, 104, 140)]
tom = Turtle()


def coloring():
    turtle.colormode(255)
    colors = random.choice(hirst_colors)
    return colors


tom.penup()
tom.hideturtle()
tom.setheading(225)
tom.forward(300)
tom.setheading(0)
tom.speed(10)

dots = 100

for x in range(1, dots+1):
    tom.dot(20, coloring())
    tom.forward(50)

    if x % 10 == 0:
        tom.setheading(90)
        tom.forward(50)
        tom.setheading(180)
        tom.forward(500)
        tom.setheading(0)


screen = Screen()
screen.exitonclick()
