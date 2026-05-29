
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
import csv

turtle.bgcolor("black")
def save_matrix(matrix,filename,n:int,num_of_colors:int,prob:list[float],radius:float):
    with open(filename,"a",newline='') as f:
        writer = csv.writer(f)
        for key, value in matrix.items():
            row = [n,num_of_colors,radius] +[x for x in prob]+ [key] + list(value.values())
            writer.writerow(row)
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

def particle_field_2(n:int,num_of_colors:int,prob:list[float] = [],radius:float=1):
    """
    Particles interact through local attraction and repulsion rules based
    on particle type. Interaction strength decreases with distance, creating
    smooth collective motion. Dense regions experience higher effective drag,
    causing clusters to stabilize over time. Small random perturbations and
    boundary noise prevent static equilibrium and sustain emergent patterns.
    """
    t_colors = ["red","blue","green","yellow","cyan","magenta","orange","purple","white"]
    true_matrix = {
        c1: {c2: round(random.uniform(-1, 1),2) for c2 in t_colors} for c1 in t_colors
    }
    turt = []
    if not prob:
        prob = [random.random() for _ in range(num_of_colors)]
        if len(prob) < len(t_colors):
            prob.extend([0]*(len(t_colors)-len(prob)))
        if len(prob) > len(t_colors):
            prob = prob[:len(t_colors)]
    
    turtle.tracer(0)
    for i in range(n):
        t = turtle.Turtle(shape="circle")
        t.color(random.choices(t_colors,k=1,weights=prob)[0])
        t.shapesize(0.5, 0.5)
        rx = random.uniform(-w2,w2)
        ry = random.uniform(-h2,h2)
        t.penup()
        t.goto(rx,ry)
        turt.append(t)
    turtle.update()
    vel = [(0,0) for _ in range(n)]
    drag = 0.1
    write = False
    while True:
        for i,t1 in enumerate(turt):
            vx,vy = vel[i]
            x1,y1 = t1.pos()
            if i == 1 and not write:
                save_matrix(true_matrix,"matrix.csv",n,num_of_colors,prob,radius)
                write = True
            for j,t2 in enumerate(turt):
                if i == j:
                    continue
                if random.random() < 0.01:
                    vx += random.uniform(-0.01,0.01)
                    vy += random.uniform(-0.01,0.01) #! to prevent the system from getting stuck in a static state, add some random noise to the velocity
                x2,y2 = t2.pos()
                hyp = math.hypot(x1-x2,y1-y2) 
                if hyp < .1:
                    continue
                #* Planned extension: combine the particle interaction system with
                #* a flow field so particles respond both to nearby particles and
                #* to large-scale environmental motion.
                if hyp < radius:
                    k = -0.000001
                    c1 = t1.pencolor()
                    c2 = t2.pencolor()
                    t1_affects = true_matrix[c1][c2]
                    vx += (t1_affects * (x2 - x1) / hyp)*math.exp(k*hyp)
                    vy += (t1_affects * (y2 - y1) / hyp)*math.exp(k*hyp)
                    # vx += (t1_affects * (x2 - x1) / hyp)*math.pow(hyp,-.5)
                    # vy += (t1_affects * (y2 - y1) / hyp)*math.pow(hyp,-.5)
                    vx *= (1-drag)
                    vy *= (1-drag)
                vel[i] = (vx,vy)
        # radius += 1
        for i,t in enumerate(turt):
            vx,vy = vel[i]
            t.setx(t.xcor() + vx)
            t.sety(t.ycor() + vy)
            x,y = t.pos()
            #! remove comments to make the system gain energy at the borders, which can lead to more interesting patterns but less stability
            if x > w2:
                t.setpos((w2-random.uniform(1,2),y))
                vx = -abs(vx) * 0.95
                vel[i] = (vx+random.uniform(-.1,.1),vy+random.uniform(-.1,.1))
            elif x < -w2:
                t.setpos((-w2+random.uniform(1,2),y))
                vx = abs(vx) * 0.95
                vel[i] = (-vx+random.uniform(-.1,.1),vy+random.uniform(-.1,.1))
            if y < -h2:
                vy = abs(vy) * 0.95
                t.setpos((x,-h2+random.uniform(1,2)))
                vel[i] = (vx+random.uniform(-.1,.1),vy+random.uniform(-.1,.1))
            elif y > h2:
                vy = -abs(vy) * 0.95    
                t.setpos((x,h2-random.uniform(1,2)))
                vel[i] = (vx+random.uniform(-.1,.1),vy+random.uniform(-.1,.1))
            if i % 1 == 0:
                t.clear()
                t.goto(x,y-radius)
                t.pendown()
                t.circle(radius)
                t.penup()
                t.goto(x,y)
        turtle.update()
# i = input()
width = turtle.window_width()
height = turtle.window_height()
w2 = width//2
h2 = height//2
particle_field_2(100,3,radius = 25)
