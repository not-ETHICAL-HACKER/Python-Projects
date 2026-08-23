
#! new idea of this version is including closeness of aletter to the target letter
#? ex: if target letter is 'a' and child letter is 'b', then the fitness score will be higher than if the child letter is 'z'
#! closeness=1−abs(ord(char[i])−ord(target[i]))/25

import random
random.seed(0)
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;':,.<>/?`~ "
char_idx = {c:i for i,c in enumerate(chars)}
pswd = "password"
n = len(pswd)
N = 125
class Creature:
    def __init__(self,id):
        self.pswd = id
        cc, cp ,cl= correct_ness(pswd, self.pswd)
        self.fitness = cc * 0.10 + cp * 0.60 + cl * 0.30
def correct_ness(target,child):
    correct_count = 0
    correct_pos = 0
    correct_distance = 0
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
            correct_distance += 1
        else:
            dist = abs(char_idx[target[i]] - char_idx[child[i]])
            correct_distance += 1 - (dist / (len(chars) - 1))
    return min(len(target),correct_count) / len(target) if target else 0, correct_pos / len(target) if target else 0, correct_distance / len(target) if target else 0
def mutate(creature:Creature,c):
    corrective = True
    c_pswd = list(creature.pswd)
    for i in range(len(pswd)):
        if random.random() < 0.25 + min(0.25,c/1000) and not corrective:
            c_pswd[i] = random.choice(chars)
        elif random.random() < 0.25 + min(0.25,c/1000) and corrective:
            if pswd[i] != c_pswd[i]:
                c_pswd[i] = random.choice(chars)
    return Creature("".join(c_pswd))
pswd_arr = [Creature("".join(random.choices(chars,k = n))) for _ in range(N)]
c = 0
best_fitness_arr = []
best_cc_arr = []
best_cp_arr = []
best_cl_arr = []
print(f"Target password: '{pswd}'",end="\n")
while True:
    c += 1
    len_arr = len(pswd_arr)
    temp = []
    weights = [creature.fitness for creature in pswd_arr]
    parents = random.choices(pswd_arr,weights=weights,k = len_arr)
    for creature_1 in parents:
        for creature_2 in parents:
            weight_1 = creature_1.fitness
            weight_2 = creature_2.fitness
            cut_1 = max(0, min(n, int(weight_1*n) + random.randint(-5,5)))
            cut_2 = max(0, min(n, int(weight_2*n) + random.randint(-5,5)))

            child_1 = Creature(creature_1.pswd[:cut_1] + creature_2.pswd[cut_1:])
            child_2 = Creature(creature_2.pswd[:cut_2] + creature_1.pswd[cut_2:])
            r = 2 + random.randint(-1,0)
            for _ in range(r):
                temp.append(random.choices([creature_1,creature_2,child_1,child_2],weights=[weight_1,weight_2,child_1.fitness,child_2.fitness],k = 1)[0])
    best_cut = N//(10)
    pswd_arr = sorted(temp,key = lambda x:x.fitness,reverse = True)[:best_cut]
    for i in range(N - best_cut):
        if random.random() < 0.25 + min(0.25,c/1000):
            pswd_arr.append(mutate(temp.pop(random.randint(0,len(temp)-1)),c))
    if len(pswd_arr) < N:
        pswd_arr += [Creature("".join(random.choices(chars,k = n))) for _ in range(N-len(pswd_arr))]
    best: Creature = max(pswd_arr,key = lambda x:x.fitness)
    cc,cp,cl = correct_ness(pswd,best.pswd)
    best_cc_arr.append(cc)
    best_cp_arr.append(cp)
    best_cl_arr.append(cl)
    print(f"Gen {c}: {best.pswd} | with fitness: {best.fitness:.3f} | correct count: {cc:.3f} | correct position: {cp:.3f} | closeness: {cl:.3f}",end="\r")
    # print(f"Gen {c}: {best.pswd} | with fitness: {best.fitness}",end="\r")
    best_fitness_arr.append(best.fitness)
    if pswd in [creature.pswd for creature in pswd_arr]:
        print(f"\nFound password '{pswd}' in {c} generations with population size {N} each generation.")
        break
    # print(f"Gen {c}: {min(pswd_arr,key = lambda x:x.fitness).pswd} with fitness: {min(pswd_arr,key = lambda x:x.fitness).fitness}")
import matplotlib.pyplot as plt

fig, ax = plt.subplots(facecolor='black')
ax.set_facecolor('black')

plt.plot(best_fitness_arr, label="Fitness", color="blue")
plt.plot(best_cc_arr, label="Correct Count", color="orange")
plt.plot(best_cp_arr, label="Correct Position", color="green")
plt.plot(best_cl_arr, label="Closeness", color="red")

#? make the axes frame visible
for spine in ax.spines.values():
    spine.set_color('white')
ax.tick_params(colors='white', which='both')
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
ax.grid(True, color='gray', linestyle='--', alpha=0.5)
legend = plt.legend(facecolor='black', edgecolor='white')
for text in legend.get_texts():
    text.set_color('white')

plt.show()