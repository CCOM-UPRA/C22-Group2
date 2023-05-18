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
    sql = ("""SELECT tracking_number, order_date, arrival_date, orders.status AS status,
    address_line1, address_line2, city, state, zipcode, 
    card_type,
    SUM(product_quantity * product_price) AS total, 
    SUM(product_quantity) AS amount 
    FROM orders 
    LEFT JOIN contains ON orders.order_id = contains.order_id 
    LEFT JOIN payment_method ON orders.payment_id = payment_method.payment_id
    LEFT JOIN shipping_address ON orders.shipping_address_id = shipping_address.shipping_address_id
    WHERE orders.order_id = %s AND orders.customer_id = %s
    GROUP BY tracking_number, order_date, arrival_date, address_line1, address_line2, card_type;""")
    
    result = list(db.query(sql, (id, session['customer'])))
    
    if len(result) > 0:
        return result.pop()
    else:
        return result

def getOrderProductsModel(id):
    db = DBConnect()
    sql = ("""SELECT name, location, product_price, product_quantity, price, image, product_quantity * product_price AS total_price 
    FROM orders RIGHT JOIN contains ON orders.order_id = contains.order_id
    LEFT JOIN product ON contains.product_id = product.product_id
    WHERE contains.order_id = %s""")
    result = db.query(sql, (id))
    return result

def addOrderModel(shipping_address, payment_method):
    db = DBConnect()
    current_date = date.today()
    arrival_date = date.today() + timedelta(days=7)
    cart = get_cart_model()
    tk = gen_tracking_number()

    try:

        print("Trying to add order")
        # Create the order
        sql = "INSERT INTO orders (customer_id, tracking_number, order_date, arrival_date, status, shipping_address_id, payment_id) VALUES(%s, %s, %s, %s, %s, %s, %s)"
        cursor = db.execute(sql, (session['customer'], tk, str(current_date), str(arrival_date), "Received", shipping_address, payment_method))

        # Get the order id
        order_id = cursor.lastrowid

        print("the order id is: ", order_id)
        # Add each item to order
        for item in cart:
            
            
            sql = "INSERT INTO contains (order_id, product_id, product_quantity, product_price) VALUES (%s, %s, %s, %s)"
            
            print("Parameters for product: ", item)
            db.execute(sql, (order_id, item['product_id'], item['product_quantity'], item['price']))
            
            print("new contains id is: ", cursor.lastrowid)
            
            sql = "UPDATE product SET stock = stock - {} WHERE product_id = %s".format(int(item['product_quantity']))
            db.execute(sql, (item['product_id']))
            print("Changed stock of product")

        db.commit()
        session['cart'] = []

    except Exception as e:
        db.rollback()
        print(f"Error occurred: {e}")
        print("Error coming from addOrderModel()")
        return None

    print("order id is ", order_id)
    return order_id

def getProductsModel():
    cart = get_cart_model()
    return cart