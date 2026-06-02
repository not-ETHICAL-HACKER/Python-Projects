import pygame,random,math
class Particle:
    def __init__(self, x, y,color,shape):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.outer_radius = 100
        self.inner_radius = 10
        self.drag = 0.01
        self.particle_size = 1
        self.color = color
        self.shape = shape
        # self.life = 100

    def update(self,p1: 'Particle',p2: 'Particle',c_matrix: dict,s_matrix: dict):
        x1,y1 = p1.x, p1.y
        x2,y2 = p2.x, p2.y
        
        x_diff = x2 - x1
        y_diff = y2 - y1
        
        hyp = math.hypot(x_diff, y_diff)

        if hyp < 1:
            return
        
        cosine = x_diff/hyp
        sine = y_diff/hyp
        #! try to make waves by making num of particles large and at start of sim make them all point in a direction and move in it for like 10 frames and then remove the vrctor force and observe whether eave nature of particles can be observed or not
        if hyp < self.inner_radius:
            self.vx += -1/math.sqrt(hyp) * cosine
            self.vy += -1/math.sqrt(hyp) * sine
        
        elif self.inner_radius < hyp < self.outer_radius:
            k = -0.005
            self.vx += (c_matrix[p1.color][p2.color] * cosine) * math.exp(k * hyp)
            self.vy += (c_matrix[p1.color][p2.color] * sine) * math.exp(k * hyp)
            
            func_name = s_matrix[p1.shape][p2.shape][1]
            func = funcs[func_name]
            
            self.vx += func(hyp) * cosine * s_matrix[p1.shape][p2.shape][0]
            self.vy += func(hyp) * sine * s_matrix[p1.shape][p2.shape][0]
        
    def move(self):
        self.x += self.vx
        self.y += self.vy
    
    def apply_drag(self):
        self.vx *= (1-self.drag)
        self.vy *= (1-self.drag)
        
    def draw(self, screen):
        if self.shape == 'circle':
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.particle_size))
    
    def border_check(self, width, height,circle=False):
        if not circle:
            if self.x < 0:
                self.x = 0
                self.vx *= -1
            elif self.x > width:
                self.x = width
                self.vx *= -1
            if self.y < 0:
                self.y = 0
                self.vy *= -1
            elif self.y > height:
                self.y = height
                self.vy *= -1
        else:
            w2 = width//2
            h2 = height//2
            radius = min(w2, h2)
            dx = self.x - w2
            dy = self.y - h2
            dist = math.hypot(dx, dy)
            if dist > radius:
                angle = math.atan2(dy, dx)
                self.x = w2 + radius * math.cos(angle)
                self.y = h2 + radius * math.sin(angle)
                self.vx *= -1
                self.vy *= -1
                
def fix_probs(prob, n, max_len):
    if hasattr(prob, 'list') or hasattr(prob, 'tuple'):
        if not prob:
            prob = [random.random() for _ in range(n)]

        prob = prob[:max_len]
        prob.extend([0] * (max_len - len(prob)))
        
        return [p/sum(prob) for p in prob]
    if hasattr(prob, 'dict'):
        keys = list(prob.keys())[:max_len]
        values = list(prob.values())[:max_len]
        total = sum(values)
        return {k: v/total for k, v in zip(keys, values)}

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
funcs = {
        # "sin":math.sin,
        # "cos":math.cos,
        # "sin_cos":lambda x: math.sin(x)*math.cos(x),
        # "sin^2-cos^2":lambda x: math.sin(x)**2 - math.cos(x)**2,
        # "inv_exp":lambda x: math.exp(-0.01*x),
        # "log_e_1p" :lambda x: math.log1p(abs(x)),
        # "inv_sqrt": lambda x: 1/math.sqrt(abs(x)) if abs(x) > 1 else 0,
        # "atan(sin,cos)":lambda x: math.atan2(math.sin(x),math.cos(x)),
        # "inv_sqr":lambda x: 1/x**2 if abs(x) > 1 else 0,
        # "neg":lambda x:-abs(x),
        # "pos":lambda x:abs(x),
        "mex_hat": lambda x: (1 - x*x/25)*math.exp(-x*x/50),
        "gauss": lambda x: math.exp(-((x-25)**2)/50)
}

n_c = 1
n_s = 1
particles: list[Particle] = []
prob_func = [random.random() for _ in range(len(funcs))]
prob_color = [random.random() for _ in range(n_c)]
prob_shape = [random.random() for _ in range(n_s)]
t_colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta']
t_dict_colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255)
}
t_shapes = ['circle', 'square', 'triangle', 'hexagon']
f_name = list(funcs.keys())
fix_probs(prob_func, len(funcs), len(funcs))
fix_probs(prob_color, n_c, len(t_colors))
fix_probs(prob_shape, n_s, len(t_shapes))
shape_size = 0.1

true_color_matrix = {
                c1: {
                    c2: round(random.uniform(-1, 1),2)
                for c2 in t_colors
            } 
        for c1 in t_colors
    }
true_shape_matrix = {
        s1: {
                    s2: (round(random.uniform(-1, 1),2) ,random.choices(f_name,k=1,weights=prob_func)[0]) 
                for s2 in t_shapes
            } 
        for s1 in t_shapes
    }

for _ in range(100):
    x = random.uniform(0, WIDTH)
    y = random.uniform(0, HEIGHT)
    color = random.choice(list(t_dict_colors.values()))
    shape = random.choice(t_shapes)
    particles.append(Particle(x, y, color, shape))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    for i, particle in enumerate(particles):
        for j, other in enumerate(particles):
            if i == j:
                # Calculate distance and apply forces based on true_color_matrix and true_shape_matrix
                continue
            particle.update(particle, other, true_color_matrix, true_shape_matrix)
            
        particle.apply_drag()
    for particle in particles:
        particle.move()
        particle.border_check(WIDTH, HEIGHT, circle=True)
        particle.draw(screen)
    pygame.display.flip()