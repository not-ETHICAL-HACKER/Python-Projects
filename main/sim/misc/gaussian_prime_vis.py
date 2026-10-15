import random,pygame,math
pygame.init()
W,H = 500,500
W2,H2 = W//2,H//2
random.seed(0)
step = 1
max_radius = 3
max_radius_sqr = max_radius**2
rect_size = 1
pos_arr = [
    ((x-W2)/step,(H2-y)/step) for x in range(0,W,step) for y in range(0,H,step)
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
clock = pygame.time.Clock()
running = True
def is_prime(n):
    if n%2 == 0 or n<2:
        return n == 2
    for i in range(3,int(n**0.5)+1,2):
        if n%i == 0:
            return False
    return True
prime_pos_arr = [num for num in pos_arr if is_prime(int((abs(num[0]**2 + num[1]**2))))]
# prime_pos_arr = [num for num in pos_arr if is_prime(math.sqrt(abs(num[0]**2 + num[1]**2)))] #! for cocnentric circles of primes
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
                (x-W2,H2-y) for x in range(0,W,step) for y in range(0,H,step)]
            prime_pos_arr = [num for num in pos_arr if is_prime((abs(num[0]**2 + num[1]**2)))]
            for num in prime_pos_arr:
                x,y = int(num[0]),int(num[1])
                pygame.draw.rect(screen,(255,255,255),pygame.Rect((x+W2,y+H2), (1,1)))
            N = len(pos_arr)
    screen.blit(fade, (0, 0)) #! make colors be white with it fading on long distances
    t = pygame.time.get_ticks() / 1000
    dt = 1e-3
    print(t,end="\r")
    # for i,num_1 in enumerate(prime_pos_arr):
    #     for j in range(i + 1, len(prime_pos_arr)):
    #         num_2 = prime_pos_arr[j]
    #         if i != j:
    #             x1,y1 = num_1
    #             x2,y2 = num_2
    #             dist_sqr = (x2-x1)**2 + (y2-y1)**2
    #             if dist_sqr < max_radius_sqr:
    #                 pygame.draw.line(screen,(255,0,0),(x1+W2,y1+H2),(x2+W2,y2+H2),1)
    #         if i % 100 == 0 and j % 100 == 0:
    #             pygame.display.update()
    
    for num in prime_pos_arr:
        x,y = int(num[0]*math.cos(num[1])),int(num[1]*math.sin(num[0]))
        pygame.draw.rect(screen,(255,255,255),pygame.Rect((x+W2,y+H2), (rect_size,rect_size)))
    pygame.display.update()
    clock.tick(60)
pygame.quit()