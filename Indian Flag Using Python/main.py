import turtle

window = turtle.Screen()
window.title("Indian Flag")
t = turtle.Turtle()

t.hideturtle()
t.speed(5)

t.penup()
t.goto(-300, 200)
t.pendown()

#orange Rectangle
#white Rectangle

t.color("orange")
t.begin_fill()
t.forward(350)
t.right(90)
t.forward(84)
t.right(90)
t.forward(350)
t.end_fill()
t.left(90)
t.forward(84)

#green Rectangle
t.color("green")
t.begin_fill()
t.forward(84)
t.left(90)
t.forward(350)
t.left(90)
t.forward(84)
t.end_fill()

# blue circle big
t.penup()
t.goto(-77,73)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(42)
t.end_fill()

# white circld small
t.penup()
t.goto(-87, 73)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(32)
t.end_fill()

# The spokes of Indian Flag
t.penup()
t.goto(-120, 73)
t.pendown()
t.pensize(1)
t.pencolor("blue")
for i in range(24):
    t.forward(30)
    t.backward(30)
    t.left(15)

t.color("gray")
t.pensize(10)
t.penup()
t.goto(-300, 200)
t.right(180)
t.pendown()
t.forward(500)
t.left(90)
t.forward(80)
t.backward(160)

turtle.done()
