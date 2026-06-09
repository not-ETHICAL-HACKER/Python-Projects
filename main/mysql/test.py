import  random
import mysql.connector as my
con  = my.connect(host="localhost",user="root",passwd="tiger",database="johan")
cursor = con.cursor()

def matrix(txt: str = "Hello World!!!") -> str:
    alpha = "".join(chr(i) for i in range(32, 128))
    alpha = "".join(random.sample(alpha, len(alpha)))
    c = 0
    fin = ""
    while True:
        c += 1
        for ch in alpha:
            fin += ch
            if ch == txt[c]:
                alpha = "".join(random.sample(alpha, len(alpha)))
                alpha=random.sample(alpha,len(alpha))
                fin += ch
                break
        if c == len(txt):
            return fin

for i in range(100):
    ...