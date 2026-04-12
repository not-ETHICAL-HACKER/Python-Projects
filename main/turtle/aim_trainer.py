import turtle
import time
import random
t = turtle.Turtle()
e = turtle.Turtle()  # enemy

t_s = turtle.Screen()
t_s.setup()
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
def draw_circle(x: int, y: int, r: int, color: str):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def aim_trainer(time_t: float, diff: int):
    assert 0 <= diff <= 10
    t.color("blue")
    e.color("red")
    turtle.bgcolor("black")
    for _ in range(diff*10):
        t.penup()
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        t.pendown()
        if random.random() > 0.5:
            draw_circle(x, y, 10, "blue")
            turtle.ontimer(lambda: t.clear, int(time_t*1000))
        else:
            draw_circle(x, y, 10, "red")
            turtle.ontimer(lambda: e.clear, int(time_t*1000))
    turtle.done()


aim_trainer(10, 10)
