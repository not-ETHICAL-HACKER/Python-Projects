from cmath import rect
import math,random,pygame
from tkinter import dialog
pygame.init()
W,H = 500,500
W2,H2 = W//2,H//2
random.seed(0)
step = 10
zoom = 100
dilation = 10
vector_len = 1
rect_size = 5
fade_const = 10
pos_arr = [
    (x,y) for x in range(0,W,step) for y in range(0,H,step)
]
screen = pygame.display.set_mode((W,H), pygame.RESIZABLE)
pygame.display.set_caption("My Simulation")
fade = pygame.Surface((W, H), pygame.SRCALPHA)
fade.fill((0, 0, 0, fade_const))   # Last number = alpha (0-255)
""" #! smaller alpha val make the trails longer
fade.fill((0,0,0,3))    # Very long trails
fade.fill((0,0,0,10))   # Medium trails
fade.fill((0,0,0,30))   # Short trails
fade.fill((0,0,0,80))   # Very short trails
"""
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            W, H = event.w, event.h
            W2,H2 = W//2,H//2
            screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
            pos_arr = [
                (x,y) for x in range(0,W,step) for y in range(0,H,step)
            ]
            fade = pygame.Surface((W, H), pygame.SRCALPHA)
            fade.fill((0, 0, 0, fade_const))
    screen.blit(fade, (0, 0)) #! make colors be white with it fading on long distances
    t = pygame.time.get_ticks() / 1000
    print(t,end="\r")
    for j in range(len(pos_arr)):
        (x,y) = pos_arr[j]
        sim_x,sim_y = x/zoom,y/zoom
        # vx = math.exp(math.cos(sim_y)) * math.sin(sim_y) * vector_len #! log unit circle
        # vy = math.exp(math.sin(sim_x)) * math.cos(sim_x) * vector_len
        
        # vx = math.exp(math.cos(sim_y)) * math.sin(t) #! fluidish movement
        # vy = math.exp(math.sin(sim_x)) * math.cos(t)
        
        # vx = math.exp(math.cos(sim_y)) * math.sin(sim_x) #! singularity formation ig?
        # vy = math.exp(math.sin(sim_x)) * math.cos(sim_y)
        
        vx = math.exp(math.cos(sim_y + t/dilation)) * math.sin(sim_x + t/dilation) * vector_len#! better dynamic movement
        vy = math.exp(math.sin(sim_x + t/dilation)) * math.cos(sim_y + t/dilation) * vector_len
        x += vx
        y += vy
        pos_arr[j] = ((x,y))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(int(x), int(y), rect_size, rect_size))
    pygame.display.update()
    clock.tick(60)
pygame.quit()