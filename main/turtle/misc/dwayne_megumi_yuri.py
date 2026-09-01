import re
import turtle
import random
import math
#! dwanye,megumi,yuri = rock,paper,scissors
screen = turtle.Screen()
player = turtle.Turtle()
helper = turtle.Turtle("turtle")

player_icon = "classic"
player.shape(player_icon)
player.speed(0)
helper.color("purple")
helper.speed(0)
player.color("purple")
turtle.bgcolor("black")

lenght = 150
breadth = 150
keys = {
    "w": False,
    "a": False,
    "s": False,
    "d": False
}

# bind all keys automatically
for key in keys:
    screen.onkeypress(lambda k=key: keys.__setitem__(k, True), key)
    screen.onkeyrelease(lambda k=key: keys.__setitem__(k, False), key)

screen.listen()

distance = 100
angle_1 = random.uniform(0,360)
density = .01 # out of 1
def spawn(dens:float,index:int,pos:tuple[float,float])->list[turtle.Turtle]:
    shapes = ["classic","turtle","circle","square","triangle"]
    col = ["red","blue","green","yellow","cyan"]
    turts = []
    for i in range(1_000):
        if random.random() <= dens:
            nx,ny = pos 
            nx += random.gauss(0,10)
            ny += random.gauss(0,10)
            t = turtle.Turtle()
            t.color(col[index]%len(col))
            t.penup()
            t.setpos((nx,ny))
            t.pendown()
            t.shape(shapes[index]%len(shapes))
            turts.append(t)
    return turts

parts = 3

def three_origins(dist,angle)->list[list[turtle.Turtle]]:
    perm = []
    for i in range(parts):
        new_angle = angle + i * 360/parts # 120 is deg in wi=hich the turt has to turn for parity ig?
        print(new_angle)
        curr_angle = angle + i * 360/parts
        rad = math.radians(curr_angle)
        r = random.uniform(dist*.5, dist * 1.5)
        x = math.cos(rad) * r
        y = math.sin(rad) * r
        helper.setheading(new_angle)
        helper.penup()
        helper.goto(x,y)
        helper.pendown()
        temp = spawn(density,i,(x,y))
        screen.update()
        perm.append(temp)
    return perm

rocks,papers,sciscors = three_origins(distance,angle_1)
def initial_speeds(t:turtle.Turtle):
    x_s = random.gauss(0,10)
    y_s = random.gauss(0,10)
    return x_s,y_s
def move(t:turtle.Turtle,pos:tuple[float,float],i_x_s=0.0,i_y_s=0.0,drag:float=0.05):#initial x and y speed speeds repectively
    x,y = pos
    i_x_s *= (1-drag)
    i_y_s *= (1-drag)
    x += i_x_s
    y += i_y_s
    if x > lenght:
        i_x_s *= -1
        x = lenght - (x-lenght)
    if x < -lenght:
        i_x_s *= -1
        x = -lenght + (-lenght-x)
    if y < -breadth:
        i_y_s *= -1
        y = -breadth + (-breadth-y)
    if y > breadth:
        i_y_s *= -1
        y = breadth - (y-breadth)
    
    t.penup()
    t.setpos((x,y))
    t.pendown()
    return x,y,i_x_s,i_y_s

rocks = [(t,initial_speeds(t)) for t in rocks]
papers = [(t,initial_speeds(t)) for t in papers]
sciscors = [(t,initial_speeds(t)) for t in sciscors]

while True:
    for i,(t, (x_s,y_s)) in enumerate(rocks):
        x,y,x_s,y_s = move(t,t.pos(),x_s,y_s)
        rocks[i] = (t,(x_s,y_s))
    for i,(t, (x_s,y_s)) in enumerate(papers):
        x,y,x_s,y_s = move(t,t.pos(),x_s,y_s)
        papers[i] = (t,(x_s,y_s))
    for i,(t, (x_s,y_s)) in enumerate(sciscors):
        x,y,x_s,y_s = move(t,t.pos(),x_s,y_s)
        sciscors[i] = (t,(x_s,y_s))
    if keys["w"]:
        player.setheading(90)
        player.forward(2)

    if keys["s"]:
        player.setheading(270)
        player.forward(2)

    if keys["a"]:
        player.setheading(180)
        player.forward(2)

    if keys["d"]:
        player.setheading(0)
        player.forward(2)

    screen.update()
    
turtle.done()