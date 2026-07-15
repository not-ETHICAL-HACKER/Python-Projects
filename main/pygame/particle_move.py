import pygame
import numpy as np
pygame.init()

WIDTH,HEIGHT = 1000,700
w2,h2 = WIDTH//2,HEIGHT//2

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Simulation")

WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255,0,0)
GREEN = (0,255,0)
BLUE  = (0,0,255)
running = True
clock = pygame.time.Clock()
num = 1_000
x_arr = [np.random.randint(0,w2*2) for _ in range(num)]
y_arr = [np.random.randint(0,h2*2) for _ in range(num)]

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
    # events
    force = 1
    keys = pygame.key.get_pressed()
    mx, my = pygame.mouse.get_pos()
    buttons = pygame.mouse.get_pressed()

    for key in range(pygame.K_0, pygame.K_9 + 1):
        if keys[key]: #! changes force expereienceed based on number pressed
            force = key - pygame.K_0
    for i in range(num):
        ux,uy = 0,0
        x,y = x_arr[i],y_arr[i]
        if buttons[0]:
            dist = max(np.hypot(x - mx,y - my),0.1)
            ux = (x - mx)/dist * force
            uy = (y - my)/dist  * force
        elif buttons[2]:
            dist = max(np.hypot(x - mx,y - my),0.1)
            ux = (mx - x)/dist * force
            uy = (my - y)/dist * force
            
        x += np.random.randint(-1,2) + ux
        y += np.random.randint(-1,2) + uy

        x = max(0, min(WIDTH, x))
        y = max(0, min(HEIGHT, y))

        x_arr[i] = x
        y_arr[i] = y
        
    screen.fill(BLACK)
    for i in range(num):
        pygame.draw.circle(screen,RED,(x_arr[i],y_arr[i]),1)
    
    pygame.display.update()
    clock.tick(60)
pygame.quit()
exit()