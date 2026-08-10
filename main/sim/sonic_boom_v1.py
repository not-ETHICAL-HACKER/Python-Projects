import pygame,math,random

pygame.init()

W,H = 500,500
running = True

screen = pygame.display.set_mode((W,H), pygame.RESIZABLE)
pygame.display.set_caption("My Simulation")

clock = pygame.time.Clock()

x = 0
y = H // 2
size  = []
ax = 1
ay = random.uniform(-1e-1,1e-1)
vx = 0
vy = 0
max_len = 110 #! recommened at 100 for consistency and not lag
circles = []

dt = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            W, H = event.w, event.h
            screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
    if len(circles) > max_len:
        circles.pop(0)
        size.pop(0)
    if x > W:
        ax = 1
        ay = random.uniform(-1e-1,1e-1)
        x = 0
        vx = vy = 0
        # y = random.randint(int(W/4),int(W-W/4))
    screen.fill((5, 2, 10))
    dt = clock.tick(120) / 10_000 #! do not change or pc explode
    # print(dt)
    # break
    ax *= 0.999
    ay *= 0.999
    vx = vx + ax * dt
    vy = vy + ay * dt 
    x += vx
    y += vy
    circles.append((x,y))
    size.append(1)
    total_circles = len(circles)
    for j in range(total_circles):
        size[j] *= 1 + dt * 50
        
        #? calculate fade ratio (0 for oldest, 1 for newest)
        fade = j / total_circles
        
        cx, cy = int(circles[j][0]), int(circles[j][1])
        r = int(size[j])

        #? shifted cyan & magenta rings
        if r < max(W, H):
            #? magenta channel (shifted slightly left)
            # pygame.draw.circle(screen, (int(180 * fade), 0, int(255 * fade)), (cx - 1, cy), r, 10)
            #? cyan channel (shifted slightly right)
            pygame.draw.circle(screen, (0, int(255 * fade), int(255 * fade)), (cx + 1, cy), r, 10)

        # pygame.draw.circle(screen, (255, 240, 150), (cx, cy), 1)
    pygame.display.update()
pygame.quit()