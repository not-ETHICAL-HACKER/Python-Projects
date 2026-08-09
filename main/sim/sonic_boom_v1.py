import pygame,math,random

pygame.init()

W,H = 500,500
running = True

screen = pygame.display.set_mode((W,H), pygame.RESIZABLE)
pygame.display.set_caption("My Simulation")

clock = pygame.time.Clock()

x = 0
y = H // 2
ax = 1
ay = 0



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            W, H = event.w, event.h
            screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)


    for j in range(A):
        pygame.draw.circle(
            screen,
            (255, 0, 255),
            (int(a_x_arr[j]), int(a_y_arr[j])),
            interaction_rad,
            1          # outline thickness
        )
        pygame.draw.circle(screen, (255,255,0), (int(a_x_arr[j]), int(a_y_arr[j])),abs_rad)