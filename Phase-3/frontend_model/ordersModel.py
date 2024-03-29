from classes.db_connect import DBConnect 
from flask import session

def get_customer_order():
    db = DBConnect()
    sql = "SELECT * FROM orders NATURAL JOIN customer NATURAL JOIN product WHERE customer_id =%s"
    result = db.query(sql, (session['customer']))
    return result

def getOrdersIDsModel(customer_id):
    db = DBConnect()
    
    sql = "SELECT order_id FROM orders WHERE customer_id = %s"
    result = db.query(sql, (customer_id))
    return result

def cancelOrderModel(order_id):
    db = DBConnect()
    
    try:
        sql = "UPDATE orders SET status = 'Cancelled' WHERE order_id = %s AND customer_id = %s"
        
        db.execute(sql, (order_id, session['customer']))
        
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error occurred: {e}")
        return None

def get_orders_and_products_model(customer_id):
    db = DBConnect()

    print("Getting orders and products")
    orders_query = ("""SELECT order_id, tracking_number, order_date, arrival_date, orders.status AS status,
    address_line1, address_line2, city, state, zipcode,
    card_type, card_name, card_number,
    SUM(product_quantity * product_price) AS total,
    SUM(product_quantity) AS amount 
    FROM orders 
    NATURAL JOIN contains 
    LEFT JOIN payment_method ON orders.payment_id = payment_method.payment_id 
    LEFT JOIN shipping_address ON orders.payment_id = shipping_address.shipping_address_id
    WHERE orders.customer_id = %s
    GROUP BY order_id
    ORDER BY order_id ASC;""")

    products_query = ("""SELECT order_id, product_id, name, image, price, product_quantity, (product_price * product_quantity) AS total_price
    FROM contains
    NATURAL JOIN product
    WHERE order_id IN (SELECT order_id FROM orders WHERE customer_id = %s);""")

    orders = db.query(orders_query, (customer_id))
    products = db.query(products_query, (customer_id))

    # Group products by order_id
    order_products = {}
    for order in orders:
        order_id = order['order_id']
        order_products[order_id] = [product for product in products if product['order_id'] == order_id]
        
        new_payment_num = '*'*(len(order['card_number']) - 4)
        last_numbers = order['card_number'][(len(order['card_number']) - 4):len(order['card_number'])]
        new_payment_num += last_numbers
        order['card_number'] = new_payment_num

    print("orders: ", [x['order_id'] for x in orders])

    # Combine order and product data into a list of tuples
    result = [(order, order_products[order['order_id']]) for order in orders]

    return result