import math,random,pygame
pygame.init()
W,H = 500,500
W2,H2 = W//2,H//2
random.seed(42)
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
clock = pygame.time.Clock()
running = True
og_time = 0
cooldown_time = .5
scale = .1
max_vel = 5
drag = .01
fluid = not True
player:list[tuple[int,int,float,float,tuple[int,int,int]]] = [(W2, H2,0,0,(255,255,255))]
class laser:
    def __init__(self, timing,vel,size,time):
        self.tx = random.randint(0,W)
        self.ty = random.randint(0,H)
        self.x = self.tx if random.random() > .5 else 0
        self.y = self.ty if not self.x else 0
        self.vel = vel
        self.dx = self.tx - self.x
        self.dy = self.ty - self.y
        self.magnitude = math.hypot(self.dx,self.dy)
        self.vx = self.dx / self.magnitude if self.magnitude != 0 else 0
        self.vy = self.dy / self.magnitude if self.magnitude != 0 else 0
        self.vx *= self.vel * math.sqrt(time)
        self.vy *= self.vel * math.sqrt(time)
        self.past_time = 0
        self.timing = timing
        self.size = size
    def draw(self):
        if pygame.time.get_ticks() - self.past_time > self.timing*1000:
            # pygame.draw.line(screen, (255,0,0), (self.x,self.y), (self.x+self.vx,self.y+self.vy), self.size)
            pygame.draw.rect(screen,(0,255,0),pygame.Rect((int(self.tx), int(self.ty), 5,5)))
            self.x += self.vx
            self.y += self.vy
            pygame.draw.rect(screen, (255,0,0), pygame.Rect((int(self.x), int(self.y), self.size,self.size)))
            self.past_time = pygame.time.get_ticks()
    def check(self):
        if self.x > W or self.y > H or self.x < 0 or self.y < 0:
            return True
        return False
    def collide(self,player_pos):
        x,y,vx,vy,color = player_pos
        dx = x - self.x
        dy = y - self.y
        mag = max(1e-3,math.hypot(dx,dy))
        if mag < self.size/2:
            return True
        return False
lasers:list[laser] = [laser(random.randint(1,2),random.randint(10,50),random.randint(25,30),pygame.time.get_ticks()/1000) for _ in range(10)]
death_timer = 0
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
                player = [(W2, H2,0,0,(255,255,255))]
    mx, my = pygame.mouse.get_pos()
    buttons = pygame.mouse.get_pressed()
    t = pygame.time.get_ticks() / 1000
    dt = 1e-3
    print(t,end="\r")
    keys = pygame.key.get_pressed()
    x,y,vx,vy,color = player[0]
    if keys[pygame.K_w]:
        vy -= scale
    if keys[pygame.K_s]:
        vy += scale
    if keys[pygame.K_a]:
        vx -= scale
    if keys[pygame.K_d]:
        vx += scale
    player[0] = (x,y,vx,vy,color)
    cooldown = t - og_time > cooldown_time
    for l in lasers:
        l.draw()
        if l.check():
            lasers.remove(l)
            lasers.append(laser(random.randint(1,2),random.randint(10,50),random.randint(25,30),pygame.time.get_ticks()/1000))
        col = l.collide(player[0])
        if col:
            print(f"You died with score {pygame.time.get_ticks()/1000-death_timer}")
            death_timer = pygame.time.get_ticks()/1000
            player = [(W2, H2,0,0,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))]
            lasers:list[laser] = [laser(random.randint(1,2),random.randint(10,50),random.randint(25,30),pygame.time.get_ticks()/1000) for _ in range(10)]
    for i, player_pos in enumerate(player):
        x,y,vx,vy,color = player_pos
        if fluid:
            x += vx
            y += vy
        else:
            vx = min(max(-max_vel,vx), max_vel) * (1-drag)
            vy = min(max(-max_vel,vy), max_vel) * (1-drag)
            x += vx 
            y += vy
        if x < 0: x = W
        elif x > W: x = 0 
        if y < 0: y = H
        elif y > H: y = 0
        player[i] = (x,y,vx,vy,color)
        pygame.draw.circle(screen, color, (int(player_pos[0]), int(player_pos[1])), 10)
    screen.blit(fade, (0, 0)) #! make colors be white with it fading on long distances
    pygame.display.update()
    clock.tick(60)
pygame.quit()