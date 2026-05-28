
"""Core concept
You have N particles of C colors. A rule matrix defines attraction/repulsion between each color pair:
        red   green   blue
red     +0.5  -0.3    +0.1
green   -0.1  +0.8    -0.5
blue    +0.3  -0.2    +0.4
Each frame, for every particle, sum up forces from all other particles based on color rules, update velocity, move.
"""
#! In Particle Life, + means attraction, - means repulsion  
import turtle
import random
import math
turtle.bgcolor("black")
def particle_field_1(n:int,radius:float=1):
    colors = ["red","blue","green"]
    shapes = ["circle","square","triangle"]
    index = {"red":0,"blue":1,"green":2}
    matrix = {
        #          red    blue   green
        "red" :   [+1.5,  -2,    -2],   #? red only loves itself, hates others
        "blue" :  [+3,   -0.1,  -0.75],  #! blue strongly likes red, slightly dislikes green, slightly dislikes itself
        "green" : [+3,   -0.75,  -0.1]  #! green strongly likes red, slightly dislikes itself, slightly dislikes blue
    }

    turt = []
    pos  = []
    drag = 0.1
    turtle.tracer(0)
    for i in range(3):
        for j in range(n):
            rx = random.randint(-w2,w2)
            ry = random.randint(-h2,h2)
            pos.append((rx,ry))
            t = turtle.Turtle(shape=shapes[i])
            t.shapesize(0.5, 0.5)
            t.color(colors[i])
            t.penup()
            t.goto(rx,ry)
            turt.append(t)
        turtle.update()
    turtle.update()
    vel = [(0,0) for _ in range(n*3)]
    while True:
        for i,t1 in enumerate(turt):
            vx,vy = vel[i]
            x1,y1 = t1.pos()
            for j,t2 in enumerate(turt):
                if i == j:
                    continue
                x2,y2 = t2.pos()
                hyp = max(math.hypot(x1-x2,y1-y2),1e-6)
                if hyp < radius:
                    k = -0.01
                    c1 = t1.pencolor()
                    c2 = t2.pencolor()
                    t1_affects = matrix[c1][index[c2]]
                    # vx += (t1_affects * (x2 - x1) / hyp)*math.exp(k*hyp)
                    # vy += (t1_affects * (y2 - y1) / hyp)*math.exp(k*hyp)
                    vx += (t1_affects * (x2 - x1) / hyp)*math.pow(hyp,-2)
                    vy += (t1_affects * (y2 - y1) / hyp)*math.pow(hyp,-2)
                    vx *= (1-drag)
                    vy *= (1-drag)
                vel[i] = (vx,vy)
        for i,t in enumerate(turt):
            vx,vy = vel[i]
            t.setx(t.xcor() + vx)
            t.sety(t.ycor() + vy)
            if t.xcor() < -w2:
                t.setx(-w2)
                vel[i] = (-vx,vy)
            elif t.xcor() > w2:
                t.setx(w2)
                vel[i] = (-vx,vy)
            if t.ycor() < -h2:
                t.sety(-h2)
                vel[i] = (vx,-vy)
            elif t.ycor() > h2:
                t.sety(h2)
                vel[i] = (vx,-vy)
        turtle.update()

width = turtle.window_width()
height = turtle.window_height()
w2 = width//2
h2 = height//2
particle_field_1(3,math.hypot(w2,h2))
