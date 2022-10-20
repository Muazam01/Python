from turtle import Turtle, Screen,colormode
from random import randint

# Different polygons:-->
# timmy = Turtle()
# timmy.shape()
# timmy.color("red")
# t=colormode(255)
# n=3
#
# game=True
# def move():
#     for i in range(n):
#         timmy.forward(80)
#         timmy.right(360 / n)
#
#
# while game:
#     move()
#     timmy.color(randint(0, 255), randint(0, 255), randint(0, 255))
#     n+=1
#     if n==10:
#         game=False
#
# screen = Screen()
# screen.exitonclick()


#_ Random walk:-->
# timmy = Turtle()
# timmy.shape()
# timmy.color("red")
# t=colormode(255)
# timmy.pensize(6)
# timmy.speed(6)
# screen = Screen()
# screen.screensize(1000,1000)
#
# run=True
# while run:
#     timmy.goto(randint(0, 500), randint(0, 500))
#     timmy.color(randint(0,255),randint(0,255),randint(0,255))

# see angela yuu's lecture for a different approach towards this problem and the
#previous problem, there the appproach taken is through the use of a list to
#randomly choose the colors, directions, etc
#screen.exitonclick()

#SpiroGraph
screen = Screen()
timmy = Turtle()
timmy.shape()
timmy.color("red")
t=colormode(255)
timmy.pensize(4)
timmy.speed(0)
timmy.home()
def spirograph(gap):
    for i in range(int(360/gap)):
        timmy.circle(50)
        current_heading = timmy.heading()
        timmy.setheading(current_heading + gap)
        timmy.color(randint(0, 255), randint(0, 255), randint(0, 255))
        timmy.circle(50)
spirograph(5)










screen.exitonclick()



