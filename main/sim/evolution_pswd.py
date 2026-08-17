import math,random
random.seed(0)
chars = "abcdefghijklmnopqrstuvwxyz"#ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;':,.<>/?`~ "
pswd = "helloworld"
n = len(pswd)
N = 10
MAX_N = 10**5
pswd_arr = ["".join(random.choices(chars,k = n)) for _ in range(N)]

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

fitness_arr = {}
for child in pswd_arr:
    noise_1 = random.random()
    cc_1, cp_1 = correct_ness(pswd, child)
    weight_1 = cc_1 * 0.25 + cp_1 * 0.70 + noise_1 * 0.05
    fitness_arr[child] = weight_1

while pswd not in pswd_arr:
    len_arr = len(pswd_arr)
    temp = []
    for i in range(len_arr):
        for j in range(len_arr):
            weight_1 = fitness_arr[pswd_arr[i]]
            weight_2 = fitness_arr[pswd_arr[j]]
            child_1 = pswd_arr[i][:int(weight_1*n)] + pswd_arr[j][int(weight_1*n):]
            child_2 = pswd_arr[j][:int(weight_2*n)] + pswd_arr[i][int(weight_2*n):]
            cc_c_1, cp_c_1 = correct_ness(pswd, child_1)
            cc_c_2, cp_c_2 = correct_ness(pswd, child_2)
            c_weight_1 = cc_c_1 * 0.25 + cp_c_1 * 0.70 + random.random() * 0.05
            c_weight_2 = cc_c_2 * 0.25 + cp_c_2 * 0.70 + random.random() * 0.05
            top_3_weights = sorted([weight_1, weight_2, c_weight_1, c_weight_2], reverse=True)[:3]
            if weight_1 in top_3_weights:
                temp.append(pswd_arr[i])
            if weight_2 in top_3_weights:
                temp.append(pswd_arr[j])
            if c_weight_1 in top_3_weights:
                temp.append(child_1)
            if c_weight_2 in top_3_weights:
                temp.append(child_2)
    pswd_arr = temp[:MAX_N]