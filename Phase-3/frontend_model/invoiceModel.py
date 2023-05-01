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
            

def gen_order_list():
    order_list = ''.join(["{}".format(randint(0, 9)) for num in range(0, 10)])
    db = DBConnect()
    # validating that order list is unique 
    sql = "SELECT DISTINCT order_list FROM order_list"
    result = db.query(sql)
    
    nums = [x['order_list'] for x in result]
    
    print(nums)
    
    print("New order list:", order_list)
    while order_list in nums:
        order_list = ''.join(["{}".format(randint(0, 9)) for num in range(0, 10)])
        print("New order_list: ", order_list)
        
    return order_list


def get_cart_model():
    if 'cart' in session:
        return session['cart']

def getOrderModel():
    orderDict2 = [] 
    order_list = gen_order_list()
    current_date = date.today()
    arrival_date = date.today() + timedelta(days=7)
    cart = get_cart_model()

    db = DBConnect()
    sql = "SELECT * FROM customer NATURAL JOIN shipping_address NATURAL JOIN payment_method WHERE customer_id = %s"
    result = db.query(sql,(session['customer'])).pop()


    for items in cart:
        tk = gen_tracking_number()
        orderDict = {
            "customer_id": session['customer'],
            "product_id": items["product_id"],
            "tracking_num": tk,
            "order_date": current_date,
            "arrival_date": arrival_date, 
            "shipping_address1": result["address_line1"],
            "shipping_address2": result["address_line2"],
            "city": result["city"],
            "state": result["state"],
            "zipcode": result["zipcode"],
            "total": items['total_price'],
            "payment_method": result["card_type"],
            "status": "Received",
            "product_quantity": items['quantity']
            }
        orderDict2.append(orderDict)
        order = tuple(orderDict.values())
        sql = "INSERT INTO orders (customer_id, product_id, tracking_number, order_date, arrival_date, shipping_address1, shipping_address2,"
        "city, state, zipcode, total, payment_method, status, product_quantity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        db.execute(sql, order)
        sql = "INSERT INTO order_list (order_id, customer_id, order_list) VALUES (last_insert_id(),%s,%s)"
        print("Executing query with order_list: ", order_list)
        db.execute(sql, (orderDict["customer_id"], order_list))

    session['cart'] = []
    return orderDict2


def getProductsModel():
    cart=get_cart_model()
    return cart
