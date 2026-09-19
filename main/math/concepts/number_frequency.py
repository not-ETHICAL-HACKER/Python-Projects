import time
n = 5 * 10**3
s_num = "67"
c = 0
leading_num = False
delay = 1
print("start")
for i in range(n+1):
    num = str(i)
    if s_num in num and not leading_num:
        # c += num.count(s_num)
        c += 1
        time.sleep(1/c*delay)
        print(f"num: {i:,} | Probability of {s_num} is {c/(n if n != 0 else 1)*100: .2f}%",end = "\r")
    if leading_num and num[0] == s_num:
        c += 1
        time.sleep(1/c*delay)
        print(f"num: {i:,} | Probability of {s_num} is {c/(n if n != 0 else 1)*100: .2f}%",end = "\r")
print()
print(f"'{s_num}' has appeared in mode {leading_num:=} in [0,{n}] {c} times\nProbability of {s_num} is {c/(n if n != 0 else 1)*100: .2f}%")
