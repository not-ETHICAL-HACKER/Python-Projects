import random
import turtle
import math

screen = turtle.Screen()
screen.tracer(0)  # turns off auto-rendering, key to no flicker


class Circle:
    def __init__(self, x: int, y: int, r: int, color: str, initial_vx: float = 0, initial_vy: float = 0):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.vx = initial_vx  # velocity
        self.vy = initial_vy  # velocity

    def update(self):
        self.x += self.vx
        self.y += self.vy
        # bounce off walls
        if random.random() > 0.5:
            sign = 1
        else:
            sign = -1
        if abs(self.x) > 400:
            self.vx *= -1
        if abs(self.y) > 400:
            self.vy *= -1
        if abs(self.x) > 450:
            self.vx = 0+random.random()*sign
            self.x = 0
        if abs(self.y) > 450:
            self.vy = 0+random.random()*sign
            self.y = 0

    def draw(self, t):
        t.penup()
        t.goto(self.x, self.y - self.r)
        t.pendown()
        t.color(self.color)
        t.circle(self.r)

    def collides(self, other):
        dist = math.hypot(self.x - other.x, self.y - other.y)
        return dist < self.r + other.r


t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.bgcolor("black")
circles = [Circle(0, 0, 30, "red", 0, 0), Circle(50, 0, 20, "cyan", .1, -.1)]

while True:
    t.clear()  # wipe frame
    for c in circles:
        c.update()
        c.draw(t)
    # check collisions
    if circles[0].collides(circles[1]):
        circles[0].vx += -1
        circles[1].vx += -1
    screen.update()  # render the new frame
