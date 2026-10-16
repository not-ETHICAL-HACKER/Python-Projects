import math,random,pygame
pygame.init()
W,H = 500,500
W2,H2 = W//2,H//2
random.seed(42)
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
og_time = 0
cooldown_time = .5
scale = 5
transverse = not True
player:list[tuple[int,int,float,float]] = [(W2, H2,0,0)]
class laser:
    def __init__(self, timing,vel,size):
        self.tx = random.randint(0,W)
        self.ty = random.randint(0,H)
        self.x = self.tx if random.random() > .5 else 0
        self.y = self.ty if not self.x else 0
        self.vel = vel
        self.past_time = 0
        self.timing = timing
        self.size = size
    def draw(self):
        if pygame.time.get_ticks() - self.past_time > self.timing*1000:
            pygame.draw.line(screen, (255,0,0), (self.x,self.y), (self.x+self.vel,self.y+self.vel), self.size)
            self.x += self.vel
            self.y += self.vel
            self.past_time = pygame.time.get_ticks()
    def check(self):
        if self.x > W or self.y > H or self.x < 0 or self.y < 0:
            return True
        return False
lasers:list[laser] = [laser(random.randint(1,5),random.randint(10,50),random.randint(1,5)) for _ in range(10)]
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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_r:
                player = [(W2, H2,0,0)]
    mx, my = pygame.mouse.get_pos()
    buttons = pygame.mouse.get_pressed()
    t = pygame.time.get_ticks() / 1000
    dt = 1e-3
    print(t,end="\r")
    keys = pygame.key.get_pressed()
    x,y,vx,vy = player[0]
    if keys[pygame.K_w]:
        vy -= scale
    if keys[pygame.K_s]:
        vy += scale
    if keys[pygame.K_a]:
        vx -= scale
    if keys[pygame.K_d]:
        vx += scale
    player[0] = (x,y,vx,vy)
    cooldown = t - og_time > cooldown_time
    for l in lasers:
        l.draw()
        if l.check():
            lasers.remove(l)
            lasers.append(laser(random.randint(1,5),random.randint(1,5),random.randint(1,5)))
    for player_pos in player:
        x,y,vx,vy = player_pos
        x += vx 
        y += vy 
        player_pos = (x,y,vx,vy)
        pygame.draw.circle(screen, (255,255,255), (int(player_pos[0]), int(player_pos[1])), 10)
    screen.blit(fade, (0, 0)) #! make colors be white with it fading on long distances
    pygame.display.update()
    clock.tick(60)
pygame.quit()