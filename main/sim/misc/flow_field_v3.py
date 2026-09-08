import pygame,math,random
pygame.init()
W,H = 500,500
D = 100
W2,H2 = W//2,H//2
random.seed(42)
step = 30
pos_arr = [
    (x,y,z) for x in range(0,W,step) for y in range(0,H,step) for z in range(0,D,step)
]

N = len(pos_arr)
screen = pygame.display.set_mode((W,H), pygame.RESIZABLE)
pygame.display.set_caption("My Simulation")
fade = pygame.Surface((W, H), pygame.SRCALPHA)
fade_const = 10
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
size = 1
k = 100
colors = [(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for _ in range(N)]
size_arr = [size for _ in range(N)]
c_avg_arr = [(sum(c)/3) for c, pos in zip(colors, pos_arr)]#[(sum(c)/3 + pos[2])/2 for c, pos in zip(colors, pos_arr)]
func_k = list(funcs.keys())
funcs_arrs = [random.choice(func_k) for _ in range(N)]
recur_depth = 10
def recur_sin_v1(x,depth,curr = 0):
    if curr >= depth:
        return x
    return math.sin(recur_sin_v1(x,depth,curr+1))
def recur_sin_v2(x,depth,curr = 0):
    if curr >= depth:
        return 0
    return math.sin(x + recur_sin_v2(x,depth,curr+1))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("Quitting...")
        elif event.type == pygame.KEYDOWN:
            pygame.display.set_caption(f"{recur_depth=}")
            if event.key == pygame.K_UP:
                recur_depth += 1
            elif event.key == pygame.K_DOWN:
                recur_depth = max(1, recur_depth - 1)
        elif event.type == pygame.VIDEORESIZE:
            W, H = event.w, event.h
            W2,H2 = W//2,H//2
            screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)

            fade = pygame.Surface((W, H), pygame.SRCALPHA)
            fade.fill((0, 0, 0, fade_const))
            pos_arr = [
                (x,y,z) for x in range(0,W,step) for y in range(0,H,step) for z in range(0,D,step)
            ]
            N = len(pos_arr)
            funcs_arrs = [random.choice(func_k) for _ in range(N)]
            colors = [(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for _ in range(N)]
            size_arr = [size for _ in range(N)]
            c_avg_arr = [(sum(c)/3) for c, pos in zip(colors, pos_arr)]#[(sum(c)/3 + pos[2])/2 for c, pos in zip(colors, pos_arr)]
    for i,pos in enumerate(pos_arr):
        x,y,z = pos
        t = pygame.time.get_ticks() / 1000 #! remove time dependency for more stable flow field
        mx = x - W/2
        my = H/2 - y
        mz = z - D/2
        c_avg = c_avg_arr[i]
        vx = (mx)/(k) + t
        vy = (my)/(k) + t
        vz = (mz)/(k) + t

        # x += funcs[funcs_arrs[i]](my/k + t)
        # y += funcs[funcs_arrs[i]](mx/k + t)
        
        # x += (math.atan2((my), (k) + t) + math.cos((my)/(k) + t)) * (c_avg/255)
        # y += (math.atan2((mx),k + t) + math.sin((mx)/(k) + t)) * (c_avg/255)
        x += recur_sin_v2(vz, recur_depth) * (c_avg/255)
        y += recur_sin_v2(vx, recur_depth) * (c_avg/255)
        z += recur_sin_v2(vy, recur_depth) * (c_avg/255)
        # x += math.cos((mz)/(k) * math.pi + t) * (c_avg/255)
        # y += math.cos((mx)/(k) * math.pi + t) * (c_avg/255)
        # z += math.cos((my)/(k) * math.pi + t) * (c_avg/255)
        size_arr[i] = min(10,max(0, size + int(10 * abs(math.sin((mz)/(k) * math.pi + t)))))

        # x = max(0,min(x,W))
        # y = max(0,min(y,H))
        # z = max(0,min(z,D))
        pos_arr[i] = (x,y,z)
    screen.blit(fade, (0, 0))
    for i in range(N):
        pygame.draw.rect(screen, colors[i], (int(pos_arr[i][0]), int(pos_arr[i][1]), size_arr[i], size_arr[i]))
    pygame.display.update()
    clock.tick(60)
pygame.quit()