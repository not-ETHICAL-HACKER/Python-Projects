import mysql.connector as my
d=my.connect(host="localhost",user="oppai_suki",password="oyakodon",database="food")
c=d.cursor()
def new_food(name:str,price:float,quantity:int)->None:
    q="insert into food_items(name,price,quantity) values(%s,%s,%s)"
    val=(name,price,quantity)
    c.execute(q,val)
    d.commit()
    print("Food item added successfully.")
new_food("Burger",5.99,50)