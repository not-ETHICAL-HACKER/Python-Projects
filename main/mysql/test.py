import  random
import mysql.connector as my
con  = my.connect(host="localhost",user="root",passwd="tiger",database="johan")
cursor = con.cursor()
products = ["apple", "banana", "orange", "grape", "kiwi"]
names = ["Alice", "Bob", "Charlie", "David", "Eve"]


for _ in range(100):
    n = random.choice(names)
    p = random.choice(products)
    q = random.randint(1, 10)
    cursor.execute(f"insert into sales values ({n}, {p}, {q},{p*q})")

con.commit()
con.close()
