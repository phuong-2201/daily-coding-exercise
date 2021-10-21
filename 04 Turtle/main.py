from turtle import Turtle, Screen
import turtle
import random

tim = Turtle()
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

## draw different shape
# for n_size in range(3, 11):
#     tim.color(random.choice(colors))
#     for i in range(n_size):
#         angle = 360 / n_size
#         tim.forward(100)
#         tim.right(angle=angle)

## random walk
# directions = [0, 90, 180, 270]
turtle.colormode(255)  # we must choose the color mode before we can use it in color()
# tim.pensize(15)  # width
tim.speed("fastest")  # speed


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


# draw a Spirograph
def draw_sprirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_sprirograph(5)

screen = turtle.Screen()
screen.exitonclick()
