import turtle
import time
import random
t = turtle.Turtle()
e = turtle.Turtle()  # enemy

t_s = turtle.Screen()
t_s.setup(600, 600)
t_s.title("Aim Trainer")
t.hideturtle()
e.hideturtle()
t.fillcolor("blue")
t.fillcolor("red")
t.speed(0)
e.speed(0)
def within(t_x: int, t_y: int,c_x: int, c_y: int, r: int) -> bool:
    return (t_x - c_x)**2 + (t_y - c_y)**2 <= r**2
#!imporoive this
def aim_trainer(time_t: float, diff: int):
    assert 0 <= diff <= 10
    t.color("blue")
    e.color("red")
    turtle.bgcolor("black")
    for i in range(diff*10):
        t.penup()
        x = random.randint(-500, 500)
        y = random.randint(-500, 500)
        t.pendown()
        if random.random() > 0.5:
            t.goto(x, y)
            t.begin_fill()
            t.circle(10)
            t.end_fill()
            turtle.ontimer(lambda: t.clear, int(time_t*1000))
        else:
            e.goto(x, y)
            e.begin_fill()
            e.circle(10)
            e.end_fill()
            turtle.ontimer(lambda: e.clear, int(time_t*1000))
    turtle.done()


aim_trainer(10, 10)
