import math,random,pygame
#! watch to get idea how to sim
#? https://youtu.be/4p7JJ6VPnTM?si=--jDbETjjw98WnsW
#! done the coulomb part 
# todo: do the second vecotr part given in the video 
pygame.init()
W,H = 500,500
W2,H2 = W//2,H//2
random.seed(0)
step = 10
vector_len = 10
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
fade_const = 100
fade.fill((0, 0, 0, fade_const))   # Last number = alpha (0-255)
""" #! smaller alpha val make the trails longer
fade.fill((0,0,0,3))    # Very long trails
fade.fill((0,0,0,10))   # Medium trails
fade.fill((0,0,0,30))   # Short trails
fade.fill((0,0,0,80))   # Very short trails
"""
clock = pygame.time.Clock()
running = True
k = 10**2
vector_sizes = [vector_len for _ in range(N)]
velocities = [(0,0) for _ in range(N)]
og_time = 0
cooldown_time = .5
transverse = not True

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
            colors = [(255,255,255) for _ in range(N)]
            vectors = [(0,0) for __ in range(N)]
            vector_sizes = [vector_len for _ in range(N)]
    screen.blit(fade, (0, 0)) #! make colors be white with it fading on long distances
    mx, my = pygame.mouse.get_pos()
    buttons = pygame.mouse.get_pressed()
    t = pygame.time.get_ticks() / 1000
    dt = 1e-3
    print(t,end="\r")
    cooldown = t - og_time > cooldown_time
    if cooldown:
        og_time = t
        if buttons[0]:
            charges.append((1,(mx,my)))
            C += 1
        elif buttons[2]:
            charges.append((-1,(mx,my)))
            C += 1
    res_x = []
    res_y = []
    for j in range(C):
        c,(qx,qy) = charges[j]
        vx = math.cos(t) * math.log(t + 1) * c
        vy = math.sin(t) * math.log(t + 1) * c
        qx += vx
        qy += vy
        charges[j] = (c,(qx,qy))
    Sum_x = [0] * N
    Sum_y = [0] * N
    for j in range(C):
        for i in range(N):
            x1,y1 = pos_arr[i]
            c,(x2,y2) = charges[j]
            vector_x = vector_y = 0

            dx = x2 - x1
            dy = y2 - y1
            hyp = max(1e-3,math.hypot(dx,dy))
            ux = dx/hyp 
            uy = dy/hyp 

            E = max(0,((max_radius - hyp)/max_radius)) * c #* pseudo electric field with fading
            vector_x = ux * vector_sizes[i] * E 
            vector_y = uy * vector_sizes[i] * E
            Sum_x[i] += vector_x
            Sum_y[i] += vector_y
    for i in range(N):
        x1,y1 = pos_arr[i]
        res_ux,res_uy = Sum_x[i], Sum_y[i]
        if abs(res_ux) < 0.1 and abs(res_uy) < 0.1:
            continue  #skip draw for dead vectors
        magnitude = math.hypot(res_ux,res_uy)
        x2 = x1 + res_ux
        y2 = y1 + res_uy
        color_intensity = max(0,min(255, int(magnitude/vector_len*255)))
        r,g,b = colors[i]
        r = color_intensity
        b = 255 - color_intensity
        g = 0
        colors[i] = r,g,b
        if transverse:
            perp_ux,perp_uy = -res_uy, res_ux
            x3 = x1 + perp_ux
            y3 = y1 + perp_uy
            # pygame.draw.line(screen, (r,b,g), (int(x1), int(y1)), (int(x2+perp_ux), int(y2+perp_uy)), 2)
            pygame.draw.line(screen, (r,b,g), (int(x1), int(y1)), (int(x3), int(y3)), 2)
        else:
            pygame.draw.line(screen, colors[i], (int(x1), int(y1)), (int(x2), int(y2)), 2)
    pygame.draw.rect(screen, (0,255,0), pygame.Rect(mx,my,10,10))
    for charge in charges:
        c,pos = charge
        x,y = pos
        pygame.draw.circle(screen, (255,0,0) if c > 0 else (0,0,255), (int(x),int(y)), 5)
    pygame.display.update()
    clock.tick(60)
pygame.quit()