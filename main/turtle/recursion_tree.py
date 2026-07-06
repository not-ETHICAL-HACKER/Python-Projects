import turtle
turtle.speed(0)
turtle.bgcolor("black")
t = turtle.Turtle(visible=False)
t.color("green")
def tree(length):
    if length < 5:
        return

    t.forward(length)
    t.pensize(length / 10)

    t.left(30)
    tree(length*0.7)
    t.pensize(length / 10)

    t.right(60)
    tree(length*0.7)
    t.pensize(length / 10)

    t.left(30)
    t.backward(length)

tree(100)