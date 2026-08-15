import random
random.seed(0)
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"#0123456789!@#$%^&*()_+-=[]{}|;':,.<>/?`~ "
pswd = "Hello World"
n = len(pswd)
N = 100
class Creature:
    def __init__(self,id):
        self.pswd = id
        cc, cp = correct_ness(pswd, self.pswd)
        random_noise = 0
        self.fitness = cc * 0.30 + cp * 0.70 + random_noise * 0.05
def correct_ness(target,child):
    correct_count = 0
    correct_pos = 0
    d_1 = {}
    d_2 = {}
    for i in target:
        d_1[i] = d_1.get(i, 0) + 1
    for i in child:
        d_2[i] = d_2.get(i, 0) + 1
    for k,v in d_1.items():
        if k in d_2:
            correct_count += min(v,d_2[k])
    for i in range(len(target)):
        if target[i] == child[i]:
            correct_pos += 1
    return correct_count / len(target) if target else 0, correct_pos / len(target) if target else 0
def mutate(creature):
    pswd = list(creature.pswd)
    for i in range(len(pswd)):
        if random.random() < 0.25:
            pswd[i] = random.choice(chars)
    return Creature("".join(pswd))
pswd_arr = [Creature("".join(random.choices(chars,k = n))) for _ in range(N)]
c = 0
while pswd not in [creature.pswd for creature in pswd_arr]:
    c += 1
    len_arr = len(pswd_arr)
    temp = []
    parents = random.choices(pswd_arr,weights=[creature.fitness for creature in pswd_arr],k = len_arr)
    for creature_1 in parents:
        for creature_2 in parents:
            weight_1 = creature_1.fitness
            weight_2 = creature_2.fitness
            cut_1 = max(0, min(n, int(weight_1*n) + random.randint(-5,5)))
            cut_2 = max(0, min(n, int(weight_2*n) + random.randint(-5,5)))

            child_1 = Creature(creature_1.pswd[:cut_1] + creature_2.pswd[cut_1:])
            child_2 = Creature(creature_2.pswd[:cut_2] + creature_1.pswd[cut_2:])
            temp.append(random.choices([creature_1,creature_2,child_1,child_2],weights=[weight_1,weight_2,child_1.fitness,child_2.fitness],k = 2 + random.randint(-1,0))[0])
    best_cut = N//(10+c//10)
    pswd_arr = sorted(temp,key = lambda x:x.fitness,reverse = True)[:best_cut]
    for i in range(N - best_cut):
        if random.random() < 0.25:
            pswd_arr.append(mutate(temp.pop(random.randint(0,len(temp)-1))))
    if len(pswd_arr) < N:
        pswd_arr += [Creature("".join(random.choices(chars,k = n))) for _ in range(N-len(pswd_arr))]
    print(f"Gen {c}: {max(pswd_arr,key = lambda x:x.fitness).pswd} with fitness: {max(pswd_arr,key = lambda x:x.fitness).fitness}")
    # print(f"Gen {c}: {min(pswd_arr,key = lambda x:x.fitness).pswd} with fitness: {min(pswd_arr,key = lambda x:x.fitness).fitness}")