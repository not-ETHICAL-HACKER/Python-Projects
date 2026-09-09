
#!  make this version use the pointers (ones in 3b1b) instead of using particles. (or maybe use both, but make the pointers more prominent)
#! the new version should be more like a flow field, where the pointers are the main focus, and the particles are just there to show the flow of the field. (maybe make the particles fade out over time, so they don't clutter the screen)
#? ex
"""
→  →  ↗  ↑  ↑  ↖  ←
→  ↗  ↑  ↑  ↖  ←  ←
↗  ↑  ↑  ↖  ←  ←  ↙
↑  ↑  ↖  ←  ←  ↙  ↓
↑  ↖  ←  @  ←  ↙  ↓
↖  ←  ←  ←  ↙  ↓  ↓
←  ←  ←  ↙  ↓  ↓  ↘
#! where the @ is the particle, and the ←  ↙  ↓ ↑  ↖ are the pointers, and the # are just empty space. The pointers should be more prominent than the particles, and the particles should fade out over time.
#! remove particles if possible
#! the pointersd should update every frame the pointers are vectors
source ●───────────────▶ head
       (x1,y1)          (x2,y2)
#! normalise and colorcode the pointers based on their direction and magnitude
#? just use a draw func btw (x1,y1) and (x2,y2) are the start and end points of the pointer, respectively
#? dont need the arrow head the line is enough to show the direction of the pointer
"""
import pygame,math,random
pygame.init()
W,H = 500,500
W2,H2 = W//2,H//2
random.seed(42)
step = 10
pos_arr = [
    (x,y) for x in range(0,W,step) for y in range(0,H,step)
]
N = len(pos_arr)
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
funcs = {
    "sin": lambda x: math.sin(x/50 + pygame.time.get_ticks()/1000) * 5,
    "cos": lambda x: math.cos(x/50 + pygame.time.get_ticks()/1000) * 5,
    "atan2": lambda x: math.atan2(math.sin(x/50 + pygame.time.get_ticks()/1000), math.cos(x/50 + pygame.time.get_ticks()/1000)) * 5,
    "log": lambda x: math.sin(math.log1p(abs(x/50 + pygame.time.get_ticks()/1000))) * 5,
    "exp": lambda x: math.exp(math.sin(x/50 + pygame.time.get_ticks()/1000)) * 5,
    "sqrt": lambda x: math.sqrt(abs(math.sin(x/50 + pygame.time.get_ticks()/1000))) * 5,
}
clock = pygame.time.Clock()
running = True
k = 100
colors = [(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for _ in range(N)]
c_avg_arr = [sum(c)/3 for c in colors]
func_k = list(funcs.keys())
funcs_arrs = [random.choice(func_k) for _ in range(N)]
vector_len = 10
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
                N = len(pos_arr)
                funcs_arrs = [random.choice(func_k) for _ in range(N)]
                colors = [(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for _ in range(N)]            
                c_avg_arr = [sum(c)/3 for c in colors]
                vectors = [(0,0) for __ in range(N)]
        new_pos_arr = []
        for i,pos in enumerate(pos_arr):
            x,y = pos
            t = pygame.time.get_ticks() / 1000 #! remove time dependency for more stable flow field
            mx = x - W/2
            my = H/2 - y
            c_avg = c_avg_arr[i]
            nx = x + math.sin((my)/(k) + t) * (c_avg/255)
            ny = y + math.cos((mx)/(k) + t) * (c_avg/255)
            # nx = x + funcs["log"](my) * (c_avg/255)
            # ny = y + funcs["log"](mx) * (c_avg/255)
            new_pos_arr.append((nx,ny))
        screen.blit(fade, (0, 0))
        for i in range(N):
            x1,y1 = pos_arr[i]
            x2,y2 = new_pos_arr[i]
            
            dx = x2 - x1
            dy = y2 - y1
            hyp = max(1e-6,math.hypot(dx,dy))
            ux = dx/hyp 
            uy = dy/hyp
            
            x2 = x1 + ux * vector_len
            y2 = y1 + uy * vector_len
            if _ == 0:
                vectors.append((ux,uy))
            else:
                oux,ouy = vectors[i]
                dot = oux*ux + ouy*uy
                if abs(dot) > math.cos(math.pi/6):
                    colors[i] = (255,0,0)
                elif abs(dot) > math.cos(math.pi/4):
                    colors[i] = (0,255,0)
                elif abs(dot) > math.cos(math.pi/3):
                    colors[i] = (0,0,255)
                else:
                    colors[i] = (255,255,255)
                pygame.draw.line(screen, colors[i], (int(x1), int(y1)), (int(x2), int(y2)), 2)
        
        pygame.display.update()
        clock.tick(60)
pygame.quit()