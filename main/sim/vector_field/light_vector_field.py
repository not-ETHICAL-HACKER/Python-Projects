import math,random,pygame
#! watch to get idea how to sim
#? https://youtu.be/4p7JJ6VPnTM?si=--jDbETjjw98WnsW
pygame.init()
W,H = 500,500
W2,H2 = W//2,H//2
random.seed(42)
step = 25
vector_len = 20
max_radius = 1000
pos_arr = [
    (x,y) for x in range(0,W,step) for y in range(0,H,step)
]
C = 2
charges = [(random.uniform(-1,1),(random.randint(0,W),random.randint(0,H))) for _ in range(C)]
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
k = 1
vector_sizes = [vector_len for _ in range(N)]
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
                charges = [(random.choice([-1,1]),(random.randint(0,W),random.randint(0,H))) for _ in range(C)]
                colors = [(255,255,255) for _ in range(N)]
                vectors = [(0,0) for __ in range(N)]
                vector_sizes = [vector_len for _ in range(N)]
        screen.blit(fade, (0, 0)) #! make colors be white with it fading on long distances
        res_x = []
        res_y = []
        t = pygame.time.get_ticks() / 1000
        for j in range(C):
            c,(qx,qy) = charges[j]
            qx += math.cos(t) * 5 * random.randint(-1,1)
            qy += math.sin(t) * 5 * random.randint(-1,1)
            charges[j] = (c,(qx,qy))
        
        res_color = []
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
                ux = dx/hyp if c > 0 else -dx/hyp
                uy = dy/hyp if c > 0 else -dy/hyp
                
                vector_x = ux * vector_sizes[i] * ((max_radius - hyp)/max_radius)
                vector_y = uy * vector_sizes[i] * ((max_radius - hyp)/max_radius)

                temp_colors[i] = [max(0, min(255, int(color_value*((max_radius - hyp)/max_radius)))) for color_value in [255]*3]
                temp_x.append(vector_x)
                temp_y.append(vector_y)
            res_x.append(temp_x)
            res_y.append(temp_y)
            res_color.append(temp_colors)
        fin_pos_arr = []
        for i in range(N):
            s_x = 0
            s_y = 0
            s_c = []
            for j in range(C):
                s_x += res_x[j][i]
                s_y += res_y[j][i]
            colors[i] = ...
            fin_pos_arr.append((s_x/C,s_y/C))
        for i in range(N):
            x1,y1 = pos_arr[i]
            avg_ux,avg_uy = fin_pos_arr[i]
            x2 = x1 + avg_ux
            y2 = y1 + avg_uy
            pygame.draw.line(screen, colors[i], (int(x1), int(y1)), (int(x2), int(y2)), 2)
            
        for charge in charges:
            c,pos = charge
            x,y = pos
            pygame.draw.circle(screen, (255,0,0) if c > 0 else (0,0,255), (int(x),int(y)), 10)
        pygame.display.update()
        clock.tick(60)
pygame.quit()