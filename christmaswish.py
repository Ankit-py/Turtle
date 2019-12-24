from turtle import *
from random import randint


def create_rectangle(turtle, color, x, y, width, height):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()

    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)

    turtle.end_fill()
    turtle.setheading(0)


def create_circle(turtle, x, y, radius, color):
    tree.penup()
    tree.color(color)
    tree.fillcolor(color)
    tree.goto(x, y)
    tree.pendown()
    tree.begin_fill()
    tree.circle(radius)
    tree.end_fill()


BG_COLOR = "#0080ff"

tree = Turtle()
tree.speed(2)
screen = tree.getscreen()
screen.bgcolor(BG_COLOR)
screen.title("Merry Christmas")
screen.setup(width=1.0, height=1.0)
y = -100

create_rectangle(tree, "red", -15, y - 60, 30, 60)

width = 240
tree.speed(10)
while width > 10:
    width = width - 10
    height = 10
    x = 0 - width / 2
    create_rectangle(tree, "green", x, y, width, height)
    y = y + height

tree.speed(1)
tree.penup()
tree.color('yellow')
tree.goto(-20, y + 10)
tree.begin_fill()
tree.pendown()
for i in range(5):
    tree.forward(40)
    tree.right(144)
tree.end_fill()

tree_height = y + 40

create_circle(tree, 230, 180, 60, "white")
create_circle(tree, 220, 180, 60, BG_COLOR)

tree.speed(10)
number_of_stars = randint(20, 30)
for _ in range(0, number_of_stars):
    x_star = randint(-(screen.window_width() // 2), screen.window_width() // 2)
    y_star = randint(tree_height, screen.window_height() // 2)
    size = randint(5, 20)
    tree.penup()
    tree.color('white')
    tree.goto(x_star, y_star)
    tree.begin_fill()
    tree.pendown()
    for i in range(5):
        tree.forward(size)
        tree.right(144)
    tree.end_fill()

tree.speed(1)
tree.penup()
msg = "Merry Christmas from Ankit Mohapatra "
tree.goto(0, -200)
tree.color("white")
tree.pendown()
tree.write(msg, move=False, align="center", font=("Arial", 15, "bold"))

tree.hideturtle()
screen.mainloop()
