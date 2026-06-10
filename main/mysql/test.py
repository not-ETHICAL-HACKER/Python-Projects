import  random
import mysql.connector as my
con  = my.connect(host="localhost",user="root",passwd="tiger",database="johan")
cursor = con.cursor()
products = ["apple", "banana", "orange", "grape", "kiwi"]
names = ["Alice", "Bob", "Charlie", "David", "Eve"]

prev = "select coalesce(max(sales_id),0) from sales"
cursor.execute(prev)
result = cursor.fetchone()
i = result[0] + 1

for _ in range(i, i + 100):
    n = random.choice(names)
    p = random.choice(products)
    q = random.randint(1, 10)
    cursor.execute(f"insert into test values ({i}, {n}, {p}, {q},{p*q})")

con.commit()
con.close()
