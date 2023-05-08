from classes.db_connect import DBConnect
from datetime import date, timedelta
from flask import session
from random import randint
import string

def gen_tracking_number():
    tracking_number = ''.join(["{}".format(randint(0, 9)) for num in range(0, 10)])
    db = DBConnect()

    # validating that the tracking number is unique 
    sql = "SELECT * FROM orders WHERE tracking_number = %s" 
    result = db.query(sql, (tracking_number))
    #print(result) 
    if result == ():
        return str(tracking_number)
    else:
        return gen_tracking_number()

def get_cart_model():
    if 'cart' in session:
        return session['cart']

def getOrderModel(id):
    db = DBConnect()
    sql = ("SELECT tracking_number, order_date, arrival_date, orders.status AS status,"
    "address_line1, address_line2, city, state, zipcode, "
    "card_type,"
    "SUM(quantity * price) AS total, "
    "SUM(quantity) AS amount "
    "FROM orders "
    "NATURAL JOIN order_item "
    "NATURAL JOIN customer "
    "NATURAL JOIN payment_method "
    "NATURAL JOIN shipping_address "
    "NATURAL JOIN product "
    "WHERE order_id = %s "
    "GROUP BY tracking_number, order_date, arrival_date,"
    "address_line1, address_line2, card_type;")
    
    result = list(db.query(sql, (id)))
    return result.pop()

def getOrderProductsModel(id):
    db = DBConnect()
    sql = ("SELECT name, location, name, price, quantity, price, image, quantity * price AS total_price "
    "FROM orders NATURAL JOIN order_item NATURAL JOIN product WHERE order_id = %s")
    result = db.query(sql, (id))
    return result

def addOrderModel():
    db = DBConnect()
    current_date = date.today()
    arrival_date = date.today() + timedelta(days=7)
    cart = get_cart_model()
    tk = gen_tracking_number()

    try:

        # Create the order
        sql = "INSERT INTO orders (customer_id, tracking_number, order_date, arrival_date, status) VALUES(%s, %s, %s, %s, %s)"
        cursor = db.execute(sql, (session['customer'], tk, current_date, arrival_date, "Received"))

        # Get the order id
        order_id = cursor.lastrowid

        # Add each item to order
        for item in cart:
            
            
            sql = "INSERT INTO order_item (order_id, product_id, quantity) VALUES (%s,%s,%s)"
            db.execute(sql, (order_id, item['product_id'], item['quantity']))
            
            sql = "UPDATE product SET stock = stock - {} WHERE product_id = %s".format(int(item['quantity']))
            db.execute(sql, (item['product_id']))

        db.commit()
        session['cart'] = []

    except Exception as e:
        db.rollback()
        print(f"Error occurred: {e}")
        return None

    return order_id

def getProductsModel():
    cart = get_cart_model()
    return cart
