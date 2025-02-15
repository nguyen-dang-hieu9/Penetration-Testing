import sqlite3
import os
from datetime import datetime
from typing import List

from models import Order, Pizza, Topping, Sauce

def create_db():
    if os.path.exists("pizza.db"):
        os.remove("pizza.db")
        
    with open('pizza.sql', 'r') as f:
        sql_code = f.read()

    conn = sqlite3.connect('pizza.db')
    conn.executescript(sql_code)

    conn.commit()
    conn.close()


def get_pizzas() -> List[Pizza]:
    conn = sqlite3.connect("pizza.db")
    cur = conn.cursor()

    cur.execute("SELECT id, name, s_price, m_price, l_price FROM pizzas")
    rows = cur.fetchall()

    pizzas = [
        Pizza(id=row[0], name=row[1], s_price=row[2], m_price=row[3], l_price=row[4])
        for row in rows
    ]

    cur.close()
    conn.close()

    return pizzas


def get_toppings() -> List[Topping]:
    conn = sqlite3.connect("pizza.db")
    cur = conn.cursor()

    cur.execute("SELECT id, name, price FROM toppings")
    rows = cur.fetchall()

    toppings = [Topping(id=row[0], name=row[1], price=row[2]) for row in rows]

    cur.close()
    conn.close()

    return toppings


def get_sauces() -> List[Sauce]:
    conn = sqlite3.connect("pizza.db")
    cur = conn.cursor()

    cur.execute("SELECT id, name, price FROM sauces")
    rows = cur.fetchall()

    sauces = [Sauce(id=row[0], name=row[1], price=row[2]) for row in rows]

    cur.close()
    conn.close()

    return sauces


def add_order(customer_name, pizza_name, pizza_size, topping, sauce):
    conn = sqlite3.connect("pizza.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT name, s_price, m_price, l_price FROM pizzas WHERE name = ?",
        (pizza_name,),
    )
    pizza_row = cur.fetchone()

    if not pizza_row:
        error = "Selected pizza does not exist"
        return error, None

    pizza_name, pizza_s_price, pizza_m_price, pizza_l_price = pizza_row

    if pizza_size == "Small":
        pizza_price = pizza_s_price
    elif pizza_size == "Medium":
        pizza_price = pizza_m_price
    elif pizza_size == "Large":
        pizza_price = pizza_l_price
    else:
        error = "Selected size  does not exist"
        return error, None

    cur.execute("SELECT name, price FROM toppings WHERE name = ?", (topping,))
    sauce_row = cur.fetchone()

    if not sauce_row:
        error = "Selected topping  does not exist"
        return error, None

    topping_name = sauce_row[0]
    topping_price = sauce_row[1]

    cur.execute("SELECT name, price FROM sauces WHERE name = ?", (sauce,))
    sauce_row = cur.fetchone()

    if not sauce_row:
        error = "Selected sauce does not exist"
        return error, None

    sauce_name = sauce_row[0]
    sauce_price = sauce_row[1]

    final_price = pizza_price + topping_price + sauce_price

    cur.execute(
        "INSERT INTO orders ( customer_name, pizza_name, size, topping, sauce, price) VALUES (?, ?, ?, ?, ?, ?)",
        (customer_name, pizza_name, pizza_size, topping_name, sauce_name, final_price),
    )

    return None, final_price
    conn.commit()
    cur.close()
    conn.close()
