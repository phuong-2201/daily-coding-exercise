import colorgram
import turtle
import random


def extract_color(image):
    colors = colorgram.extract(image, 100)
    for color in colors:
        rgb = [color.rgb for color in colors]
        colors_list = [(item.r, item.g, item.b) for item in rgb]
        return colors_list


tim = turtle.Turtle()
tim.penup()
turtle.colormode(255)
tim.speed("fastest")
colors = extract_color("image.jpg")
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for i in range(10):
    if i % 2 == 0:
        for j in range(10):
            tim.dot(20, random.choice(colors))
            tim.fd(50)
        tim.left(90)
        tim.fd(50)
        tim.left(90)
        tim.fd(50)
    else:
        for j in range(10):
            tim.dot(20, random.choice(colors))
            tim.fd(50)
        tim.right(90)
        tim.fd(50)
        tim.right(90)
        tim.fd(50)

tim.hideturtle()

screen = turtle.Screen()
screen.exitonclick()
