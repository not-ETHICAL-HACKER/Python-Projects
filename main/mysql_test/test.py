import  random,winsound
import mysql
import mysql.connector
con  = mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="johan")
cursor = con.cursor()
products = ["apple", "banana", "orange", "grape", "kiwi","mango", "pear", "peach", "plum", "watermelon","pineapple", "strawberry", "blueberry", "raspberry", "blackberry", "cherry", "coconut", "fig", "guava", "lemon", "lime", "papaya", "passionfruit", "pomegranate", "tangerine", "cantaloupe", "honeydew", "nectarine", "persimmon", "starfruit"]
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy", "Kevin", "Linda", "Michael", "Nancy", "Oscar", "Pam", "Quinn", "Rachel", "Steve", "Tracy", "Uma", "Victor", "Wendy", "Xander", "Yvonne", "Zach","Aaron", "Beth", "Cameron", "Diana", "Ethan", "Fiona", "Gavin", "Hannah", "Isaac", "Jasmine", "Kyle", "Lily", "Mason", "Nina", "Owen", "Paige", "Quincy", "Riley", "Samantha", "Tyler", "Ursula", "Violet", "Wyatt", "Ximena", "Yara", "Zane"] 
l = []
name_weights = [random.random() for _ in range(len(names))]
product_weights = [random.random() for _ in range(len(products))]

for _ in range(100_000):
    n = random.choices(names, weights=name_weights)[0]
    p = random.choices(products, weights=product_weights)[0]
    price = random.uniform(1.0, 10.0)
    q = random.randint(1, 10)
    l.append((n, p, q, price))
cursor.executemany(
        "INSERT INTO sales (customer_name, product, quantity, price) VALUES (%s, %s, %s, %s)",
        l
    )
winsound.Beep(1000, 500)  # Beep sound
con.commit()
con.close()