import math,random,pygame
#! watch to get idea how to sim
#? https://youtu.be/4p7JJ6VPnTM?si=--jDbETjjw98WnsW
#! done the coulomb part 
# todo: do the second vecotr part given in the video 
pygame.init()
W,H = 500,500
W2,H2 = W//2,H//2
random.seed(42)
step = 50
vector_len = 50
max_radius = 1000
pos_arr = [
    (x,y) for x in range(0,W,step) for y in range(0,H,step)
]
C = 1
charges = [(random.choice([-1,1]),(random.randint(0,W),random.randint(0,H))) for _ in range(C)]
N = len(pos_arr)
colors = [(255,255,255) for _ in range(N)]
screen = pygame.display.set_mode((W,H), pygame.RESIZABLE)
pygame.display.set_caption("My Simulation")
fade = pygame.Surface((W, H), pygame.SRCALPHA)
fade_const = 50
fade.fill((0, 0, 0, fade_const))   # Last number = alpha (0-255)
""" #! smaller alpha val make the trails longer
fade.fill((0,0,0,3))    # Very long trails
fade.fill((0,0,0,10))   # Medium trails
fade.fill((0,0,0,30))   # Short trails
fade.fill((0,0,0,80))   # Very short trails
"""
clock = pygame.time.Clock()
running = True
k = 10**3
vector_sizes = [vector_len for _ in range(N)]
acclerations = [(0,0) for _ in range(N)]
velocities = [(0,0) for _ in range(N)]
og_time = 0
cooldown_time = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            W, H = event.w, event.h
            W2,H2 = W//2,H//2
            screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)

            fade = pygame.Surface((W, H), pygame.SRCALPHA)
            fade.fill((0, 0, 0, fade_const))
            pos_arr = [
                    (x,y) for x in range(0,W,step) for y in range(0,H,step)
            ]
            N = len(pos_arr)
            velocities = [(0,0) for _ in range(N)]
            acclerations = [(0,0) for _ in range(N)]
            colors = [(255,255,255) for _ in range(N)]
            vectors = [(0,0) for _ in range(N)]
            vector_sizes = [vector_len for _ in range(N)]

    screen.blit(fade, (0, 0)) #! make colors be white with it fading on long distances

    mx, my = pygame.mouse.get_pos()
    buttons = pygame.mouse.get_pressed()

    t = pygame.time.get_ticks() / 1000
    dt = 1e-2
    # print(t,end="\r")
    cooldown = t - og_time > cooldown_time
    if cooldown:
        og_time = t
        if buttons[0]:
            charges.append((1,(mx,my)))
            C += 1
        elif buttons[2]:
            charges.append((-1,(mx,my)))
            C += 1

    for j in range(C):
        c,(qx,qy) = charges[j]
        ax,ay = acclerations[j]
        vx,vy = velocities[j]
        ax = max(-2,min(2,ax + random.uniform(0,1)))
        ay = max(-2,min(2,ay + random.uniform(0,1)))
        vx += math.cos(t) * ax * dt
        vy += math.sin(t) * ay * dt
        qx += vx
        qy += vy
        charges[j] = (c,(qx,qy))
        acclerations[j] = ax,ay
        velocities[j] = vx,vy
    res_x = []
    res_y = []
    res_color:list[list[tuple[int,int,int]]] = []
    for j in range(C):
        temp_x = []
        temp_y = []
        temp_colors = []
        for i in range(N):
            x1,y1 = pos_arr[i]
            c,(x2,y2) = charges[j]
            vector_x = vector_y = 0

            dx = x2 - x1
            dy = y2 - y1
            hyp = max(1e-3,math.hypot(dx,dy))
            ux = dx/hyp 
            uy = dy/hyp 

            ax,ay = acclerations[j]
            vx,vy = velocities[j]

            E = max(0,((max_radius - hyp)/max_radius)) * c #* pseudo electric field with fading
            E_t = k * (c * uy)
            E_xt = E_t * (ax/(vx**2 + 1))
            E_yt = E_t * (ay/(vy**2 + 1))
            print((E_xt,E_yt) if E_xt or E_yt else "",end = "\r")
            vector_x = min(75,ux * vector_sizes[i] * E + abs(E_xt))
            vector_y = min(75,uy * vector_sizes[i] * E + abs(E_yt))
            t_c = [255,255,255] #! comment if u want fading colors
            # t_c = [max(0, min(255, int(255*((max_radius - hyp)/max_radius)))) for _ in range(3)] #! comment if u want const colors

            temp_colors.append(t_c)
            temp_x.append(vector_x)
            temp_y.append(vector_y)
        res_x.append(temp_x)
        res_y.append(temp_y)
        res_color.append(temp_colors)
    fin_unit_vector_arr = []
    for i in range(N):
        s_x = 0
        s_y = 0
        s_c = (0,0,0)
        for j in range(C):
            s_x += res_x[j][i]
            s_y += res_y[j][i]
            s1,_,_ = s_c
            s1 += res_color[j][i][0]
            s_c = (s1,)*3
        s,_,_ = s_c
        s_c = (int(s/C),) * 3
        colors[i] = s_c
        fin_unit_vector_arr.append((s_x,s_y))
    for i in range(N):
        x1,y1 = pos_arr[i]
        res_ux,res_uy = fin_unit_vector_arr[i]
        x2 = x1 + res_ux
        y2 = y1 + res_uy
        pygame.draw.line(screen, colors[i], (int(x1), int(y1)), (int(x2), int(y2)), 2)
            
    for charge in charges:
        c,pos = charge
        x,y = pos
        pygame.draw.circle(screen, (255,0,0) if c > 0 else (0,0,255), (int(x),int(y)), 5)
    pygame.display.update()
    clock.tick(60)
pygame.quit()