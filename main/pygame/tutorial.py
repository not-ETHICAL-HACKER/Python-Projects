import pygame
pygame.init()

WIDTH,HEIGHT = 1000,700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Simulation")

WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255,0,0)
GREEN = (0,255,0)
BLUE  = (0,0,255)

"""
#! example

rect1.colliderect(rect2)

keys = pygame.key.get_pressed()

if keys[pygame.K_w]:
    y -= 5

if keys[pygame.K_SPACE]:
    print("Jump")

mx, my = pygame.mouse.get_pos()

buttons = pygame.mouse.get_pressed()

if buttons[0]:
    print("Left click")
"""

"""
v = pygame.Vector2(3,4)

v.length()

v.normalize()

v.rotate(45)

v.dot(other)
"""
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
    # events
    screen.fill(BLACK)
    font = pygame.font.SysFont(None,30)

    text = font.render(
        "Velocity = 100",
        True,
        WHITE
    )

    screen.blit(text,(20,20))
    # physics
    pygame.draw.circle(screen,RED,(200,150),25)
    # draw
    pygame.draw.line(screen,WHITE,(0,0),(400,300),3)
    pygame.draw.rect(screen,BLUE,(100,100,50,80))
    pygame.draw.polygon(screen,GREEN,[(100,100),(150,50),(200,100)])

    pygame.display.update()
    clock.tick()
pygame.quit()
exit()