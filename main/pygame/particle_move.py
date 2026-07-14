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
    for i in range(num):
        ux,uy = 0,0
        x,y = x_arr[i],y_arr[i]
        x += np.random.randint(-1,2)
        y += np.random.randint(-1,2)
        mx, my = pygame.mouse.get_pos()

        buttons = pygame.mouse.get_pressed()
        if buttons[0]:
            dist = max(np.hypot(x - mx,y - my),0.1)
            ux = (x - mx)/dist
            uy = (y - my)/dist
        elif buttons[2]:
            dist = max(np.hypot(x - mx,y - my),0.1)
            ux = (mx - x)/dist
            uy = (my - y)/dist
            
        if x < 0:
            x = 0
        if y < 0:
            y = 0
        if x > w2*2:
            x = w2*2
        if y > h2*2:
            y = h2*2
        x_arr[i] = x + ux
        y_arr[i] = y + uy
    
    screen.fill(BLACK)
    for i in range(num):
        pygame.draw.circle(screen,RED,(x_arr[i],y_arr[i]),1)
    
    pygame.display.update()
    clock.tick()
pygame.quit()
exit()