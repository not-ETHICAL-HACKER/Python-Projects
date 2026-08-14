import math,random
random.seed(0)
chars = "abcdefghijklmnopqrstuvwxyz"#ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;':,.<>/?`~ "
pswd = "helloworld"
n = len(pswd)
N = 10
MAX_N = 1000
pswd_arr = ["".join(random.choices(chars,k = n)) for _ in range(N)]

while pswd not in pswd_arr:
    len_arr = len(pswd_arr)
    temp = []
    for i in range(len_arr):
        for j in range(len_arr):
            weight_1 = random.random()
            weight_2 = 1 - weight_1
            child_1 = pswd_arr[i][:int(weight_1*n)] + pswd_arr[j][int(weight_1*n):]
            child_2 = pswd_arr[j][:int(weight_2*n)] + pswd_arr[i][int(weight_2*n):]
            print(child_1)
            print(child_2)
    break