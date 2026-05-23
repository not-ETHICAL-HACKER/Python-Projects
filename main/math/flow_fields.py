
# * FLOW FIELDS
# every point on screen has an angle (direction)
#! N turtles each follow the angle at their current position, step, repeat
# dont clear trails - let them accumulate
# angle can be defined as:
#   sin(x) * cos(y)          -> smooth rippling lanes, easy starting point
#   perlin noise              -> organic, needs 'noise' library
#   distance from a point     -> spiral/galaxy effect
#   time-varying field        -> field shifts while particles are moving
# the screen slowly fills with flowing lines

#! each frame, for each turtle:
#! 1. get current x, y
#! 2. angle = sin(rad(x)) * cos(rad(y)) * 360  (or whatever field formula)
#! 3. setheading(degrees(angle))
#! 4. forward(step_size)
#! 5. repeat, don't clear
import turtle
import random
import time
import math

t = turtle.Turtle()
t.color("blue")
turtle.bgcolor("black")
t.speed(0)
width = turtle.window_width()
height = turtle.window_height()
def mark_every(num: float):
    if num > 1000:
        return
    marker = turtle.Turtle(visible=False)
    marker.speed(0)
    marker.color("white")
    w = turtle.window_width() // 2
    h = turtle.window_height() // 2
    x = -w
    while x <= w:
        y = -h
        while y <= h:
            marker.penup()
            marker.goto(x, y)
            marker.dot(3)
            y += num
        x += num
    turtle.update()
# print(width, height)
def flow_fields_1(pos:tuple[float,float],colors:str,multipler:float=1.0):
    if not pos:
        x,y = t.xcor(),t.ycor()
    x,y = pos
    turtle.tracer(0)
    # time.sleep(2)
    for i in range(10**3+1):
        if i % 10 == 0:
            turtle.update()
        angle = math.sin(math.radians(x)*multipler)*math.cos(math.radians(y)*multipler)*360
        #print(angle)
        #t.setheading(math.degrees(angle))
        t.left(angle)
        t.forward(1*scale)
        x,y = t.pos()
        rx = random.uniform(10,50)
        ry = random.uniform(10,50)
        if x < -width//2:
            t.setx(-width//2+rx)
            t.setheading(random.randint(0,360))
        elif x > width//2:
            t.setx(width//2-rx)
            t.setheading(random.randint(0,360))
        if y < -height//2:
            t.sety(-height//2+ry)
            t.setheading(random.randint(0,360))
        elif y > height//2:
            t.sety(height//2-ry)
            t.setheading(random.randint(0,360))
            
def flow_fields_2(turt_nums: int, poss: list[tuple], multiplier: float = 1.0):
    if not poss:
        poss = [(random.uniform(-width//2, width//2), random.uniform(-height//2, height//2)) for _ in range(turt_nums)]
    
    turts = []
    for i in range(turt_nums): # add one more for center
        tt = turtle.Turtle(visible=False)
        tt.speed(0)
        tt.color(colors[i % len(colors)])
        tt.penup()
        tt.goto(poss[i])
        tt.pendown()
        turts.append(tt)

    positions = list(poss)
    num = 10**4
    
    for i in range(num + 1):
        turtle.title(f"Flow Fields - Percentage {(i/num)*100}%")
        if i % 1_000 == 0:
            turtle.update()
        for idx, tt in enumerate(turts):
            x, y = positions[idx]
            angle = math.sin(math.radians(x) * multiplier) * math.cos(math.radians(y) * multiplier) * 360
            tt.left(angle)
            tt.forward(scale)
            x, y = tt.pos()
            # boundary
            rx, ry = random.uniform(10,50), random.uniform(10,50)
            if x < -width//2: tt.setx(-width//2+rx); tt.setheading(random.randint(0,360))
            elif x > width//2: tt.setx(width//2-rx); tt.setheading(random.randint(0,360))
            if y < -height//2: tt.sety(-height//2+ry); tt.setheading(random.randint(0,360))
            elif y > height//2: tt.sety(height//2-ry); tt.setheading(random.randint(0,360))
            positions[idx] = tt.pos()

scale = 1
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

turtle.tracer(0)
mark_every(10)
flow_fields_2(10**3,[])
turtle.done()
