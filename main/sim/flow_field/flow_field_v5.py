import pygame
import math
import random
pygame.init()

W, H = 500, 500
W2, H2 = W//2, H//2
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption("My Simulation")
fade = pygame.Surface((W, H), pygame.SRCALPHA)
fade_const: int = 25
fade.fill((0, 0, 0, fade_const))   # Last number = alpha (0-255)
clock = pygame.time.Clock()
random.seed(42)

step: int = 25
vector_len: int = 50
pos_arr: list[tuple[int, int]] = [
    (x, y) for x in range(0, W, step) for y in range(0, H, step)
]

N: int = len(pos_arr)
running: bool = True
k: int = 1
colors: list[tuple[int, int, int]] = [(random.randint(0, 255), random.randint(
    0, 255), random.randint(0, 255)) for _ in range(N)]
c_avg_arr: list[float] = [sum(c)/3 for c in colors]
particle_pos: list[tuple[int, int]] = []
P: int = len(particle_pos)
old_vectors: list[tuple[float, float]] = [(0, 0) for __ in range(N)]
grid = {}
c = 0
for i, x in enumerate(range(0, W, step)):
    for j, y in enumerate(range(0, H, step)):
        c += 1
        grid[(x//step, y//step)] = c
grid = {(x//step, y//step): i+j for i, x in enumerate(range(0, W, step))
        for j, y in enumerate(range(0, H, step))}
print(grid)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            W, H = event.w, event.h
            W2, H2 = W//2, H//2
            screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)

            fade = pygame.Surface((W, H), pygame.SRCALPHA)
            fade.fill((0, 0, 0, fade_const))
            pos_arr = [
                (x, y) for x in range(0, W, step) for y in range(0, H, step)
            ]
            N: int = len(pos_arr)
            P: int = len(particle_pos)
            colors: list[tuple[int, int, int]] = [(random.randint(0, 255), random.randint(
                0, 255), random.randint(0, 255)) for _ in range(N)]
            c_avg_arr: list[float] = [sum(c)/3 for c in colors]
            new_vectors: list[tuple[float, float]] = []
            old_vectors: list[tuple[float, float]] = [
                (0, 0) for __ in range(N)]
            grid = {(x//step, y//step): i+j for i, x in enumerate(range(0, W, step))
                    for j, y in enumerate(range(0, H, step))}
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                particle_pos.append(
                    (random.randint(0, W), random.randint(0, H)))
                P = len(particle_pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                particle_pos.append(event.pos)
                P = len(particle_pos)
    new_pos_arr: list[tuple[float, float]] = []
    for i, pos in enumerate(pos_arr):
        x, y = pos
        t = 0  # ? because it is zero the vector field is static and not moving, but if you want to make it dynamic you can set it to pygame.time.get_ticks() / 1000
        mx = x - W/2
        my = H/2 - y
        c_avg = c_avg_arr[i]
        nx = x - (math.cos(2*(my)/(k) + t)) * (c_avg/255) * 5
        ny = y + (math.cos(2*(mx)/(k) + t)) * (c_avg/255) * 5
        new_pos_arr.append((nx, ny))
    screen.blit(fade, (0, 0))

    new_vectors: list[tuple[float, float]] = []
    for i in range(N):
        x1, y1 = pos_arr[i]
        x2, y2 = new_pos_arr[i]

        dx = x2 - x1
        dy = y2 - y1
        hyp = max(1e-6, math.hypot(dx, dy))
        ux = dx/hyp
        uy = dy/hyp

        x2 = x1 + ux * vector_len
        y2 = y1 + uy * vector_len
        new_vectors.append((ux, uy))
        oux, ouy = old_vectors[i]
        dot = oux*ux + ouy*uy
        if dot > 0:
            colors[i] = ((255*(dot*10) % 256), 10*(255/2-255/2*dot) % 256, 0)
        else:
            colors[i] = (0, 1.1*(255/2+255/2*dot) %
                         256, 10*(255*abs(dot)) % 256)
        pygame.draw.line(screen, colors[i], (int(
            x1), int(y1)), (int(x2), int(y2)), 2)
    old_vectors = new_vectors
    for i, pos in enumerate(particle_pos.copy()):
        x, y = pos
        ix, iy = math.floor(x/step), math.floor(y/step)
        index = grid[(ix, iy)]
        ux, uy = new_vectors[index]
        t = pygame.time.get_ticks() / 1000
        mx = x - W/2
        my = H/2 - y
        c_avg = 255  # ! make the particles white
        x += ux
        y += uy
        if x < 0:
            particle_pos.pop(i)
            continue
        if x > W:
            particle_pos.pop(i)
            continue
        if y < 0:
            particle_pos.pop(i)
            continue
        if y > H:
            particle_pos.pop(i)
            continue
        particle_pos[i] = (x, y)
        P = len(particle_pos)
    for j in range(P):
        x1, y1 = particle_pos[j]
        pygame.draw.circle(screen, (255, 255, 255), (int(x1), int(y1)), 3)
    clock.tick(60)
    pygame.display.update()

pygame.quit()
