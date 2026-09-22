import math,random,pygame
#! watch to get idea how to sim
#? https://youtu.be/4p7JJ6VPnTM?si=--jDbETjjw98WnsW
pygame.init()
W,H = 500,500
W2,H2 = W//2,H//2
C = 1
random.seed(42)
step = 25
vector_len = 50
max_radius = 250
pos_arr = [
    (x,y) for x in range(0,W,step) for y in range(0,H,step)
]
charges = [(random.choice([-1,1]),(random.randint(0,W),random.randint(0,H))) for _ in range(C)]
N = len(pos_arr)
screen = pygame.display.set_mode((W,H), pygame.RESIZABLE)
pygame.display.set_caption("My Simulation")
fade = pygame.Surface((W, H), pygame.SRCALPHA)
fade_const = 25
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
colors = [(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for _ in range(N)]
vector_sizes = [vector_len for _ in range(N)]
c_avg_arr = [sum(c)/3 for c in colors]
def coulomb_force(Q,Q_pos,vector,v_size=vector_len):
    x,y = vector
    qx,qy = Q_pos
    dx = qx - x
    dy = qy - y
    r = math.hypot(dx, dy)
    if r < 1e-3:
        return (0,0)
    F = Q/(r)
    if r > max_radius:
        F = 0
    ux = dx/r
    uy = dy/r
    return ux*F,uy*F,min(vector_len,F*(max_radius - r))
while running:
    for _ in range(2):
        if _ == 0:
            vectors = []
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
                C = 1
                N = len(pos_arr)
                charges = [(random.choice([-1,1]),(random.randint(0,W),random.randint(0,H))) for _ in range(C)]
                colors = [(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for _ in range(N)]            
                c_avg_arr = [sum(c)/3 for c in colors]
                vectors = [(0,0) for __ in range(N)]
                vector_sizes = [vector_len for _ in range(N)]
        big_pos_arr = []
        for j,charge in enumerate(charges):
            new_pos_arr = []
            c,pos = charge
            qx,qy = pos
            for i,pos in enumerate(pos_arr):
                x,y = pos
                t = pygame.time.get_ticks() / 1000 #! remove time dependency for more stable flow field
                mx = x
                my = y
                m_qx = qx
                m_qy = qy
                # c_avg = c_avg_arr[i]
                print(t,end="\r")
                nx,ny,F = coulomb_force(c,(m_qx,m_qy),(mx,my),vector_sizes[i])
                vector_sizes[i] = F*0.5 + vector_sizes[i]*0.5
                nx = x + nx
                ny = y + ny
                new_pos_arr.append((nx,ny))
            qx += math.cos(t) * 5
            qy += math.sin(t) * 5
            charges[j] = (c,(qx,qy))
            big_pos_arr.append(new_pos_arr)
        screen.blit(fade, (0, 0))
        for i in range(N):
            x1,y1 = pos_arr[i]
            x2,y2 = new_pos_arr[i]
            
            dx = x2 - x1
            dy = y2 - y1
            hyp = max(1e-3,math.hypot(dx,dy))
            ux = dx/hyp 
            uy = dy/hyp
            
            x2 = x1 + ux * vector_sizes[i]
            y2 = y1 + uy * vector_sizes[i]
            if _ == 0:
                # vectors.append((ux,uy))
                vectors.append((1,0)) #! just use a constant vector for now
            else:
                oux,ouy = vectors[i]
                dot = oux*ux + ouy*uy
                if dot > 0:
                    colors[i] = (int(255*dot),int(255/2-255/2*dot),0)
                else:
                    colors[i] = (0,int(255/2+255/2*dot),int(255*abs(dot)))
                # pygame.draw.rect(screen, colors[i], (int(x1)-2, int(y1)-2, 10, 10))
                pygame.draw.line(screen, colors[i], (int(x1), int(y1)), (int(x2), int(y2)), 2)
        for charge in charges:
            c,pos = charge
            x,y = pos
            pygame.draw.circle(screen, (255,0,0) if c > 0 else (0,0,255), (int(x),int(y)), 10)
        pygame.display.update()
        clock.tick(60)
pygame.quit()