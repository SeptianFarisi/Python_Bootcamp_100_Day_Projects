###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
from turtle import Turtle, Screen
from random import choice

colors = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
          (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86),
          (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
          (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
          (107, 127, 153), (176, 192, 208), (168, 99, 102)]

kura = Turtle()
screen = Screen()
kura.ht()
kura.speed("fastest")
screen.colormode(255)

def dot():
    for _ in range(10):
        kura.penup()
        kura.dot(20, choice(colors))
        kura.forward(50)
        if _ > 10:
            break

x = [(-225,-200),(-225,-150),(-225,-100),(-225,-50),(-225,0),(-225,50),(-225,100),(-225,150),(-225,200),
     (-225,250)]

kura.penup()
for _ in range(10):
    kura.setposition(x[_])
    dot()

screen.exitonclick()