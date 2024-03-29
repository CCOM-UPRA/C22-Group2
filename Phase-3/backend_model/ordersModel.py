from classes.db_connect import DBConnect 
# from backend_model.profileModel import MagerDicts
#
# # ORDER 1
# # ------------------------------------------------------------
# #
# orderDict1 = {"1": {
#     "tracking_num": "71287249",
#     "order_date": "01/17/23",
#     "arrival_date": "01/20/23",
#     "address_line_1": "Vista Azulin Calle 11 L13",
#     "address_line_2": "Arecibor Puerto Ricor, 00614",
#     "total": 144.97,
#     'total_items': 3,
#     "payment_method": "Mastercard",
#     'status': 'received'
# }}
#
# # ORDER 2
# # ------------------------------------------------------------
# #
# orderDict2 = {'2': {
#     "tracking_num": "92391290",
#     "order_date": "01/17/23",
#     "arrival_date": "01/20/23",
#     "address_line_1": "Vista Azulin Calle 11 L13",
#     "address_line_2": "Arecibor Puerto Ricor, 00614",
#     "total": 109.97,
#     'total_items': 3,
#     "payment_method": "Mastercard",
#     'status': 'delivered'
#
# }}
#
# # ORDER 3
# # ------------------------------------------------------------
# #
# orderDict3 = {'3': {
#     "tracking_num": "85277469",
#     "order_date": "01/17/23",
#     "arrival_date": "01/20/23",
#     "address_line_1": "Vista Azulin Calle 11 L13",
#     "address_line_2": "Arecibor Puerto Ricor, 00614",
#     "total": 49.98,
#     'total_items': 2,
#     "payment_method": "Mastercard",
#     'status': 'processed'
# }}
#
# # ORDER 4
# # ------------------------------------------------------------
# #
# orderDict4 = {'4': {
#     "tracking_num": "66788539",
#     "order_date": "01/17/23",
#     "arrival_date": "01/20/23",
#     "address_line_1": "Vista Azulin Calle 11 L13",
#     "address_line_2": "Arecibor Puerto Ricor, 00614",
#     "total": 24.99,
#     "total_items": 1,
#     "payment_method": "Mastercard",
#     'status': 'cancelled'
# }}
#
#
#
# # PRODUCTS
# # ------------------------------------------------------------
# productDict1 = {"1": {
#     "image": 'goldenballcactus.jpg',
#     "name": 'Golden Ball Cactus',
#     "family type": 'Cactus',
#     "price": 64.99,
#     "quantity": 1,
#     "total_price": 64.99,
#     "order_id": '1'
# }}
#
# productDict2 = {"2": {
#     "image": 'rose.jpg',
#     "name": 'Rose',
#     "family type": 'Flowers',
#     "price": 39.99,
#     "quantity": 2,
#     "total_price": 79.98,
#     "order_id": '1'
# }}
#
# productDict3 = {"3": {
#     "image": 'MonsteraDeliciosa.jpg',
#     "name": 'Monstera Deliciosa',
#     "family type": 'Araceae',
#     "price": 34.99,
#     "quantity": 2,
#     "total_price": 69.98,
#     "order_id": '2'
# }}
#
# productDict4 = {"4": {
#     "image": 'anthurium.jpg',
#     "name": 'Anthurium',
#     "family type": 'Araceae',
#     "price": 39.99,
#     "quantity": 1,
#     "total_price": 39.99,
#     "order_id": '2'
# }}
#
# productDict5 = {"5": {
#     "image": 'mooncactus.jpg',
#     "name": 'Moon Cactus',
#     "family type": 'Cactus',
#     "price": 24.99,
#     "quantity": 2,
#     "total_price": 49.98,
#     "order_id": '3'
# }}
#
# productDict6 = {"6": {
#     "image": 'sunflower.jpg',
#     "name": 'Sunflower',
#     "family type": 'Flowers',
#     "price": 24.99,
#     "quantity": 1,
#     "total_price": 24.99,
#     "order_id": '4'
# }}
#
#
# ordersList = MagerDicts(orderDict1, orderDict2)
# ordersList = MagerDicts(ordersList, orderDict3)
# ordersList = MagerDicts(ordersList, orderDict4)
#
# productsList = MagerDicts(productDict1, productDict2)
# productsList = MagerDicts(productsList, productDict3)
# productsList = MagerDicts(productsList, productDict4)
# productsList = MagerDicts(productsList, productDict5)
# productsList = MagerDicts(productsList, productDict6)
#

def ordersModel():
    db = DBConnect()
    sql = """SELECT orders.order_id, tracking_number, status, order_date, arrival_date, 
    SUM(product_quantity * product_price) AS total
    FROM orders
    LEFT JOIN contains ON orders.order_id = contains.order_id 
    GROUP BY orders.order_id;"""
    result = db.query(sql)
    return result 


def getordermodel(ID):
    
    if ID == '' or ID == None:
        return []
    
    db = DBConnect()
    sql = """SELECT order_id,order_date, arrival_date, orders.status,
    SUM(product_quantity * product_price) AS total, first_name, last_name, address_line1, address_line2, city, state, zipcode,
    SUM(product_quantity) as total_items
    FROM orders
    NATURAL JOIN contains
    LEFT JOIN customer ON orders.customer_id = customer.customer_id
    LEFT JOIN payment_method ON orders.payment_id = payment_method.payment_id
    LEFT JOIN shipping_address ON orders.shipping_address_id = shipping_address.shipping_address_id
    WHERE order_id = %s
    GROUP BY order_id"""
    result=db.query(sql, (ID))
    if len(result) > 0:
        return list(result).pop()
    else:
        return []

def getorderproductsmodel(ID):
    
    if ID == '' or ID == None:
        return []
    
    db = DBConnect()
    sql = ("SELECT product_id, image, name, plant_type, price, product_quantity, SUM(product_quantity * product_price) AS total FROM product NATURAL JOIN contains WHERE order_id = %s")
    result=db.query(sql, (ID))
    return result


def edit_order(Status, ID):
    print("JMMMMM")
    print(Status +" "+ ID)
    db = DBConnect()
    try:
        sql = ("UPDATE orders SET status = %s where order_id = %s")
        db.execute(sql, (Status, ID))
        db.commit()
    except Exception as e:
        print("NOOOOOO")
        db.rollback()
        print(f"Error occurred: {e}")

    
