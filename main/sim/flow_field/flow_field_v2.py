import pygame,math,random
pygame.init()
W,H = 500,500
W2,H2 = W//2,H//2
random.seed(42)
step = 20
pos_arr = [
    (x,y) for x in range(0,W,step) for y in range(0,H,step)
]
N = len(pos_arr)
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
funcs = {
    "sin": lambda x: math.sin(x/50 + pygame.time.get_ticks()/1000) * 5,
    "cos": lambda x: math.cos(x/50 + pygame.time.get_ticks()/1000) * 5,
    "atan2": lambda x: math.atan2(math.sin(x/50 + pygame.time.get_ticks()/1000), math.cos(x/50 + pygame.time.get_ticks()/1000)) * 5,
    "log": lambda x: math.log(abs(math.sin(x/50 + pygame.time.get_ticks()/1000)) + 1) * 5,
    "exp": lambda x: math.exp(math.sin(x/50 + pygame.time.get_ticks()/1000)) * 5,
    "sqrt": lambda x: math.sqrt(abs(math.sin(x/50 + pygame.time.get_ticks()/1000))) * 5,
}
clock = pygame.time.Clock()
running = True
size = 10
k = 100
colors = [(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for _ in range(N)]
c_avg_arr = [sum(c)/3 for c in colors]
func_k = list(funcs.keys())
funcs_arrs = [random.choice(func_k) for _ in range(N)]
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
            funcs_arrs = [random.choice(func_k) for _ in range(N)]
            colors = [(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for _ in range(N)]            
            c_avg_arr = [sum(c)/3 for c in colors]
    for i,pos in enumerate(pos_arr):
        x,y = pos
        t = pygame.time.get_ticks() / 1000 #! remove time dependency for more stable flow field
        mx = x - W/2
        my = H/2 - y
        c_avg = c_avg_arr[i]

        # x += funcs[funcs_arrs[i]](my/k + t)
        # y += funcs[funcs_arrs[i]](mx/k + t)
        
        # x += (math.atan2((my), (k) + t) + math.cos((my)/(k) + t)) * (c_avg/255)
        # y += (math.atan2((mx),k + t) + math.sin((mx)/(k) + t)) * (c_avg/255)
        # x += math.cos((my)/(k) + t) * (c_avg/255)
        # y += math.cos((mx)/(k) + t) * (c_avg/255)
        x += math.cos((my)/(k) * math.pi + t) * (c_avg/255)
        y += math.cos((mx)/(k) * math.pi + t) * (c_avg/255)

        # x = max(0,min(x,W))
        # y = max(0,min(y,H))
        pos_arr[i] = (x,y)
    screen.blit(fade, (0, 0))
    for i in range(N):
        pygame.draw.rect(screen, colors[i], (int(pos_arr[i][0]), int(pos_arr[i][1]), size, size))
    pygame.display.update()
    clock.tick(60)
pygame.quit()