
"""Core concept
You have N particles of C colors. A rule matrix defines attraction/repulsion between each color pair:
        red   green   blue
red     +0.5  -0.3    +0.1
green   -0.1  +0.8    -0.5
blue    +0.3  -0.2    +0.4
Each frame, for every particle, sum up forces from all other particles based on color rules, update velocity, move.
"""
#! In Particle Life, + means attraction, - means repulsion  
from encodings.punycode import T
import pickle
import turtle
import random
import math
import csv

turtle.bgcolor("black")
def save_matrix(matrix,filename,n:int,num_of_colors:int,prob:list[float],radius:float):
    """Saves the interaction matrix and parameters to a CSV file for later analysis."""
    with open(filename,"a",newline='') as f:
        writer = csv.writer(f)
        for key, value in matrix.items():
            row = [n,num_of_colors,radius] +[x for x in prob]+ [key] + list(value.values())
            writer.writerow(row)
def particle_field_1(n:int,radius:float=1):
    """THe og particle interaction / life sim"""
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
    """Planned extensions:
- Add gravity wells that attract particles within a certain radius, creating swirling patterns and acting as attractors in the system."""
    t_colors = ["red","blue","green","yellow","cyan","magenta","orange","purple","white"]
    true_matrix = {
        c1: {c2: round(random.uniform(-1, 1),2) for c2 in t_colors} for c1 in t_colors
    }
    turt = []
    print("len(t_colors) =", len(t_colors))
    print("len(prob) =", len(prob))
    if not prob:
        prob = [random.random() for _ in range(num_of_colors)]
        if len(prob) < len(t_colors):
            prob.extend([0]*(len(t_colors)-len(prob)))
        if len(prob) > len(t_colors):
            prob = prob[:len(t_colors)]
    if prob:
        if len(prob) < len(t_colors):
            prob.extend([0]*(len(t_colors)-len(prob)))
        if len(prob) > len(t_colors):
            prob = prob[:len(t_colors)]
    print("len(t_colors) =", len(t_colors))
    print("len(prob) =", len(prob))
    turtle.tracer(0)
    for i in range(n):
        t = turtle.Turtle(shape="circle")
        t.color(random.choices(t_colors,k=1,weights=prob)[0])
        t.shapesize(0.125, 0.125)
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
                    k = -0.001
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
            #!  removiing gravity wells for now bcs im dont know how to balance them, but they can add interesting dynamics by creating swirling patterns and acting as attractors in the system
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
        
def save_matrices(matrix1,matrix2,filename,n:int,radius:float):
    with open(filename, 'ab') as f:
        pickle.dump((matrix1, matrix2, n, radius), f)
        
def fix_probs(prob, n, max_len):
    if not prob:
        prob = [random.random() for _ in range(n)]

    prob = prob[:max_len]
    prob.extend([0] * (max_len - len(prob)))

    return prob
def particle_field_3(n:int,num_of_colors:int,num_of_shapes:int,prob_col:list[float] = [],prob_shape:list[float] = [],prob_func:list[float] = [],radius:float=1):
    """ adds shapes as an extra parameter to the interaction matrix, so certain colors can be attracted to specific shapes and repelled by others, creating more complex and varied patterns.This shape-based interaction adds another layer of complexity and can lead to the emergence of distinct clusters based on both color and shape, enhancing the diversity of patterns in the system."""
    
    turts = []
    og_pos = []
    t_colors = ["red","blue","green","yellow","cyan","magenta","orange","purple","white"]
    t_shapes = ["circle","square","triangle","turtle","arrow"]
    
    prob_col = fix_probs(prob_col, num_of_colors, len(t_colors))
    prob_shape = fix_probs(prob_shape, num_of_shapes, len(t_shapes))
    prob_func = fix_probs(prob_func, len(funcs), len(funcs))
    
    turtle.tracer(0)
    
    for _ in range(n):
        
            t = turtle.Turtle(shape=random.choices(t_shapes,k=1,weights=prob_shape)[0])
            t.color(random.choices(t_colors,k=1,weights=prob_col)[0])
            t.shapesize(shape_size, shape_size)
            rx = random.uniform(-w2,w2)
            ry = random.uniform(-h2,h2)
            t.penup()
            t.goto(rx,ry)
            og_pos.append((rx,ry))
            turts.append(t)
        
    turtle.update()
    
    vel = [(0,0) for _ in range(n)]
    drag = 0.1
    true_color_matrix = {
                c1: {
                    c2: round(random.uniform(-1, 1),2)
                for c2 in t_colors
            } 
        for c1 in t_colors
    }
    
    f_name = list(funcs.keys())
    
    true_shape_matrix = {
        s1: {
                    s2: (round(random.uniform(-1, 1),2) ,random.choices(f_name,k=1,weights=prob_func)[0]) 
                for s2 in t_shapes
            } 
        for s1 in t_shapes
    }
    save_matrices(true_color_matrix,true_shape_matrix,"matrices.pkl",n,radius)
    resp = set() # this is to store all turts to be respawned later, to prevent the system from losing too many particles and becoming static, which can happen if particles get stuck in a corner or cluster and can't escape due to lack of energy. By respawning them at their original positions with zero velocity, we can keep the system dynamic and allow for new interactions to occur.
    while True:
        for i,t1 in enumerate(turts):
            vx,vy = vel[i]
            x1,y1 = t1.pos()
            c1 = t1.pencolor()
            s1 = t1.shape()
            for j,t2 in enumerate(turts):
                if i == j:
                    continue
                if random.random() < 0.01:
                    vx += random.uniform(-0.01,0.01)
                    vy += random.uniform(-0.01,0.01) #! to prevent the system from getting stuck in a static state, add some random noise to the velocity
                
                x2,y2 = t2.pos()
                hyp = math.hypot(x1-x2,y1-y2) 
                
                if hyp < .1:
                    continue
                
                if hyp < radius:
                    k = -0.001
                
                    c2 = t2.pencolor()
                    s2 = t2.shape()
                    
                    t1_color_affects = true_color_matrix[c1][c2]
                    shape_affects, func = true_shape_matrix[s1][s2]
                    func = funcs[func]
                    
                    dx = x2 - x1
                    dy = y2 - y1
                    
                    cosine = dx/hyp #* this is the trig func and it acts like a unit circle, giving the direction of the force
                    sine = dy/hyp #! cos is x corr of unit vector, sin is y corr of unit vector
                    
                    decay = math.exp(k*hyp) #* this is the decay function, which makes the force weaker as the distance increases
                    
                    vx += (t1_color_affects * cosine)*decay
                    vy += (t1_color_affects * sine)*decay
                    
                    shape_force = shape_affects * func(hyp)
                    
                    vx += shape_force * cosine
                    vy += shape_force * sine
                    
                    vx *= (1-drag)
                    vy *= (1-drag) # uncomment to observe group enegy loss
                
                    vx = max(min(vx,5),-5)
                    vy = max(min(vy,5),-5)
                
                vel[i] = (vx,vy)
            
            # vx *= (1-drag) # comment out to observe stricter energy loss, which can lead to more stable clusters but less dynamic patterns
            # vy *= (1-drag)
        for i,t in enumerate(turts):
            vx,vy = vel[i]
            t.setx(t.xcor() + vx)
            t.sety(t.ycor() + vy)
            x,y = t.pos()
            x_y_hyp = math.hypot(x,y)
            sqr = True
            respawn = True
            if len(turts) <= int(len(resp)*0.75):
                for rt in resp:
                    idx = turts.index(rt)
                    rt.goto(og_pos[idx])
                    vel[idx] = (0,0)
                resp = set()
            if sqr:
            
                if x > w2:
                    t.setx(w2-random.uniform(1,2))
                    ux = x/x_y_hyp
                    uy = y/x_y_hyp
                    dot = vx*ux + vy*uy
                    
                    vx = (vx - 2*dot*ux) * 0.90 
                    vy = (vy - 2*dot*uy) * 0.95
                    
                    vel[i] = (vx+random.uniform(-.1,.1),vy+random.uniform(-.1,.1))
            
                elif x < -w2:
                    t.setx(-w2+random.uniform(1,2))
                    
                    ux = x/x_y_hyp
                    uy = y/x_y_hyp
                    dot = vx*ux + vy*uy
                    
                    vx = (vx - 2*dot*ux) * 0.90
                    vy = (vy - 2*dot*uy) * 0.90
                    vel[i] = (vx+random.uniform(-.1,.1),vy+random.uniform(-.1,.1))
            
                if y < -h2:
                    t.sety(-h2+random.uniform(1,2))
                    ux = x/x_y_hyp
                    uy = y/x_y_hyp
                    
                    dot = vx*ux + vy*uy
                    
                    vx = (vx - 2*dot*ux)*0.90
                    vy = (vy - 2*dot*uy)*0.90
                    vel[i] = (vx+random.uniform(-.1,.1),vy+random.uniform(-.1,.1))
            
                elif y > h2:
                    t.sety(h2-random.uniform(1,2))
                    ux = x/x_y_hyp
                    uy = y/x_y_hyp
                    
                    dot = vx*ux + vy*uy
                    
                    vx = (vx - 2*dot*ux) * 0.90
                    vy = (vy - 2*dot*uy) * 0.90
                    vel[i] = (vx+random.uniform(-.1,.1),vy+random.uniform(-.1,.1))
            
            else:
                true_rad = math.hypot(w2,h2)
                r = math.hypot(x,y)
            
                if r > true_rad:
                    nx = x/r
                    ny = y/r

                    dot = vx*nx + vy*ny

                    vx = vx - 2*dot*nx
                    vy = vy - 2*dot*ny

                    vel[i] = (vx,vy)
            
            if respawn:
                if x > w2 or x < -w2 or y < -h2 or y > h2:
                    resp.add(t)
                    
            if i % 1 == 0:
                t.clear()
                t.goto(x,y-radius)
                t.pendown()
                t.circle(radius)
                t.penup()
                t.goto(x,y)
        
        turtle.update()

def particle_field_4(n:int,num_of_colors:int,num_of_shapes:int,prob_col:list[float] = [],prob_shape:list[float] = [],prob_func:list[float] = [],inner_radius:float=1,outer_radius:float=100):
    """intoduces inner radius and outer radius for interactions, so particles only interact with others that are within a certain distance range, which can create more complex and varied patterns by allowing for both short-range and long-range interactions. This can lead to the emergence of distinct clusters based on proximity, as well as larger-scale structures formed by long-range forces."""
    turts = []
    t_colors = ["red","blue","green","yellow","cyan","magenta","orange","purple","white"]
    t_shapes = ["circle","square","triangle","turtle","arrow"]
    
    prob_col = fix_probs(prob_col, num_of_colors, len(t_colors))
    prob_shape = fix_probs(prob_shape, num_of_shapes, len(t_shapes))
    prob_func = fix_probs(prob_func, len(funcs), len(funcs))
    
    turtle.tracer(0)
    
    for _ in range(n):
        
            t = turtle.Turtle(shape=random.choices(t_shapes,k=1,weights=prob_shape)[0])
            t.color(random.choices(t_colors,k=1,weights=prob_col)[0])
            t.shapesize(shape_size, shape_size)
            rx = random.uniform(-w2,w2)
            ry = random.uniform(-h2,h2)
            t.penup()
            t.goto(rx,ry)
            turts.append(t)
        
    turtle.update()
    
    vel = [(0,0) for _ in range(n)]
    drag = 0.1
    true_color_matrix = {
                c1: {
                    c2: round(random.uniform(-1, 1),2)
                for c2 in t_colors
            } 
        for c1 in t_colors
    }
    
    f_name = list(funcs.keys())
    
    true_shape_matrix = {
        s1: {
                    s2: (round(random.uniform(-1, 1),2) ,random.choices(f_name,k=1,weights=prob_func)[0]) 
                for s2 in t_shapes
            } 
        for s1 in t_shapes
    }
    save_matrices(true_color_matrix,true_shape_matrix,"matrices_new.pkl",n,(inner_radius,outer_radius))
    while True:
        for i,t1 in enumerate(turts):
            vx,vy = vel[i]
            x1,y1 = t1.pos()
            c1 = t1.pencolor()
            s1 = t1.shape()
            for j,t2 in enumerate(turts):
                if i == j:
                    continue
                if random.random() < 0.01:
                    vx += random.uniform(-0.01,0.01)
                    vy += random.uniform(-0.01,0.01) #! to prevent the system from getting stuck in a static state, add some random noise to the velocity
                
                x2,y2 = t2.pos()
                hyp = math.hypot(x1-x2,y1-y2) 
                
                if hyp < .1:
                    continue
                
                if hyp < inner_radius:
                    ...
                elif inner_radius < hyp < outer_radius:
                    k = -0.0005
                
                    c2 = t2.pencolor()
                    s2 = t2.shape()
                    
                    t1_color_affects = true_color_matrix[c1][c2]
                    shape_affects, func = true_shape_matrix[s1][s2]
                    func = funcs[func]
                    
                    dx = x2 - x1
                    dy = y2 - y1
                    
                    cosine = dx/hyp #* this is the trig func and it acts like a unit circle, giving the direction of the force
                    sine = dy/hyp #! cos is x corr of unit vector, sin is y corr of unit vector
                    
                    decay = math.exp(k*hyp) #* this is the decay function, which makes the force weaker as the distance increases
                    
                    vx += (t1_color_affects * cosine)*decay
                    vy += (t1_color_affects * sine)*decay
                    
                    shape_force = shape_affects * func(hyp)
                    
                    vx += shape_force * cosine
                    vy += shape_force * sine
                    
                    vx *= (1-drag)
                    vy *= (1-drag) # uncomment to observe group enegy loss
                
                    vx = max(min(vx,5),-5)
                    vy = max(min(vy,5),-5)
                
                vel[i] = (vx,vy)
            
            # vx *= (1-drag) # comment out to observe stricter energy loss, which can lead to more stable clusters but less dynamic patterns
            # vy *= (1-drag)
        for i,t in enumerate(turts):
            vx,vy = vel[i]
            t.setx(t.xcor() + vx)
            t.sety(t.ycor() + vy)
            x,y = t.pos()
            x_y_hyp = math.hypot(x,y)
            sqr = True
            
            if sqr:
            
                if x > w2:
                    t.setx(w2-random.uniform(1,2))
                    ux = x/x_y_hyp
                    uy = y/x_y_hyp
                    dot = vx*ux + vy*uy
                    
                    vx = (vx - 2*dot*ux) * 0.90 
                    vy = (vy - 2*dot*uy) * 0.95
                    
                    vel[i] = (vx+random.uniform(-.1,.1),vy+random.uniform(-.1,.1))
            
                elif x < -w2:
                    t.setx(-w2+random.uniform(1,2))
                    
                    ux = x/x_y_hyp
                    uy = y/x_y_hyp
                    dot = vx*ux + vy*uy
                    
                    vx = (vx - 2*dot*ux) * 0.90
                    vy = (vy - 2*dot*uy) * 0.90
                    vel[i] = (vx+random.uniform(-.1,.1),vy+random.uniform(-.1,.1))
            
                if y < -h2:
                    t.sety(-h2+random.uniform(1,2))
                    ux = x/x_y_hyp
                    uy = y/x_y_hyp
                    
                    dot = vx*ux + vy*uy
                    
                    vx = (vx - 2*dot*ux)*0.90
                    vy = (vy - 2*dot*uy)*0.90
                    vel[i] = (vx+random.uniform(-.1,.1),vy+random.uniform(-.1,.1))
            
                elif y > h2:
                    t.sety(h2-random.uniform(1,2))
                    ux = x/x_y_hyp
                    uy = y/x_y_hyp
                    
                    dot = vx*ux + vy*uy
                    
                    vx = (vx - 2*dot*ux) * 0.90
                    vy = (vy - 2*dot*uy) * 0.90
                    vel[i] = (vx+random.uniform(-.1,.1),vy+random.uniform(-.1,.1))
            
            else:
                true_rad = math.hypot(w2,h2)
                r = math.hypot(x,y)
            
                if r > true_rad:
                    nx = x/r
                    ny = y/r

                    dot = vx*nx + vy*ny

                    vx = vx - 2*dot*nx
                    vy = vy - 2*dot*ny

                    vel[i] = (vx,vy)
            
            # if i % 1 == 0:
            #     t.clear()
            #     t.goto(x,y-outer_radius)
            #     t.pendown()
            #     t.circle(outer_radius)
            #     t.penup()
            #     t.goto(x,y-inner_radius)
            #     t.pendown()
            #     t.circle(inner_radius)
            #     t.penup()
            #     t.goto(x,y)
        
        turtle.update()

    
# i = input()

funcs = {
        # "sin":math.sin,
        # "cos":math.cos,
        # "sin_cos":lambda x: math.sin(x)*math.cos(x),
        # "sin^2-cos^2":lambda x: math.sin(x)**2 - math.cos(x)**2,
        # "inv_exp":lambda x: math.exp(-0.01*x),
        "log_e_1p" :lambda x: math.log1p(abs(x)),
        # "inv_sqrt": lambda x: 1/math.sqrt(abs(x)),
        # "atan(sin,cos)":lambda x: math.atan2(math.sin(x),math.cos(x)),
        # "inv_sqr":lambda x: 1/x**2 if abs(x) > 1 else 0,
        # "neg":lambda x:-abs(x),
        # "mex_hat": lambda x: (1 - x*x/25)*math.exp(-x*x/50),
        # "gauss": lambda x: math.exp(-((x-10)**2)/20)
}

width = turtle.window_width()
height = turtle.window_height()
w2 = width//2
h2 = height//2

n_c = 2
n_s = 1
shape_size = 0.1
particle_field_4(200,n_c,n_s,[1/n_c]*n_c,[1/n_s]*n_s,[1/len(funcs)]*len(funcs),outer_radius=100,inner_radius=20)
