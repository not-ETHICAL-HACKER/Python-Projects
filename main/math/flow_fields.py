
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

t = turtle.Turtle(visible=False)
t.color("blue")
turtle.bgcolor("black")
t.speed(0)
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
            
def flow_fields_2(turt_nums: int, positions: list[tuple], multiplier: float = 1.0):
    if not positions:
        positions = [(random.uniform(-width//2, width//2), random.uniform(-height//2, height//2)) for _ in range(turt_nums)]
    turts = []
    thresholds = [100, 200, 300, 400, 500, 600]
    
    for i in range(turt_nums): # add one more for center
        value = math.hypot(positions[i][0],positions[i][1])
        val = sum(1 for t in thresholds if value > t)
        tt = turtle.Turtle(visible=False)
        tt.speed(0)
        tt.color(colors[val])
        tt.color("red") # for testing
        tt.penup()
        tt.goto(positions[i])
        tt.pendown()
        turts.append(tt)

    num = 10**4
    avg = 0
    k = math.pi/180 * multiplier
    w2 = width//2
    h2 = height//2
    
    for i in range(num + 1):
        tim = time.time()
        if i % 10 == 0:
            turtle.update()
        for idx, tt in enumerate(turts):
            if i % 10 == 0:
                tt.clear()
            x, y = positions[idx]
            
            # angle = math.sin(math.radians(x) * multiplier) * math.cos(math.radians(y) * multiplier) * 360
            angle = (math.sin(x * k) * math.cos(y * k)) * 360
            tt.left(angle)
            tt.forward(1*scale)
            # boundary
            x, y = tt.xcor(), tt.ycor()
            
            # if x < -w2: rx = random.uniform(10,50); tt.setx(-w2+rx); tt.setheading(random.randint(0,360))
            # elif x > w2: rx = random.uniform(10,50); tt.setx(w2-rx); tt.setheading(random.randint(0,360))
            # if y < -h2: ry = random.uniform(10,50); tt.sety(-h2+ry); tt.setheading(random.randint(0,360))
            # elif y > h2: ry = random.uniform(10,50); tt.sety(h2-ry); tt.setheading(random.randint(0,360))
            positions[idx] = tt.pos()
        fps =1/(time.time()-tim)
        avg += fps
        if i % 10 == 0:
            turtle.title(f"Flow Fields - Percentage {(i/num)*100:.2f}% , avg:{avg/1 if i == 0 else avg/i:.2f}")

scale = 1
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

i = input()
width = turtle.window_width()
height = turtle.window_height()

turtle.tracer(0)
mark_every(100)
flow_fields_2(10**3*5,[],1)
turtle.done()
