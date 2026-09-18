import time
n = 10**5
s_num = "1"
c = 0
leading_num = True
print("start")
for i in range(n+1):
    num = str(i)
    if s_num in num and not leading_num:
        # c += num.count(s_num)
        c += 1
        time.sleep(1/c)
        print(f"num: {i:,} | Probability of {s_num} is {c/(n if n != 0 else 1)*100: .2f}%",end = "\r")
    if leading_num and num[0] == s_num:
        c += 1
        time.sleep(1/c)
        print(f"num: {i:,} | Probability of {s_num} is {c/(n if n != 0 else 1)*100: .2f}%",end = "\r")
print()
print(f"'{s_num}' has appeared in [0,{n}] {c} times\nProbability of {s_num} is {c/(n if n != 0 else 1)*100: .2f}%")