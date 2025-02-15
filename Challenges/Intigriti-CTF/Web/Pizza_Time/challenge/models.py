from typing import List

class Pizza:
    def __init__(self, id: int, name: str, s_price: float, m_price: float, l_price: float):
        self.id = id
        self.name = name
        self.s_price = s_price
        self.m_price = m_price
        self.l_price = l_price


class Topping:
    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price


class Sauce:
    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price


class Order:
    def __init__(self, id: int, pizza_name: str, toppings: List[int], sauce_name: str, customer_name: str, price: float):
        self.id = id
        self.pizza_name = pizza_name
        self.toppings = toppings
        self.sauce_name = sauce_name
        self.customer_name = customer_name
        self.price = price