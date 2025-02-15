CREATE TABLE pizzas (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    s_price REAL NOT NULL,
    m_price REAL NOT NULL,
    l_price REAL NOT NULL
);

INSERT INTO pizzas (name, s_price, m_price, l_price) VALUES ('Margherita', 8.99, 10.99, 12.99);
INSERT INTO pizzas (name, s_price, m_price, l_price) VALUES ('Pepperoni', 10.99, 12.99, 14.99);
INSERT INTO pizzas (name, s_price, m_price, l_price) VALUES ('Vegetarian', 9.99, 11.99, 13.99);
INSERT INTO pizzas (name, s_price, m_price, l_price) VALUES ('Meat Lovers', 12.99, 14.99, 16.99);
INSERT INTO pizzas (name, s_price, m_price, l_price) VALUES ('Hawaiian', 11.99, 13.99, 15.99);

CREATE TABLE toppings (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL

);

INSERT INTO toppings (name, price) VALUES
  ("Mushrooms", 0.23),
  ("Mushrooms", 0.22),
  ("Onions", 0.21),
  ("Sausage", 0.89),
  ("Bacon", 1.10),
  ("Extra cheese", 0.67),
  ("Black olives",0.45),
  ("Green peppers", 0.20),
  ("Pineapple", 0.12),
  ("Spinach", 0.10);

CREATE TABLE sauces (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL

);

INSERT INTO sauces (name, price) VALUES
  ("Marinara", 0.50),
  ("Alfredo", 0.50),
  ("BBQ", 0.70),
  ("Ranch", 0.50),
  ("Garlic butter", 0.60);

CREATE TABLE orders (
  id INTEGER PRIMARY KEY,
  customer_name TEXT NOT NULL,
  pizza_name TEXT NOT NULL,
  size TEXT NOT NULL,
  topping TEXT NOT NULL,
  sauce TEXT NOT NULL,
  price REAL NOT NULL
);