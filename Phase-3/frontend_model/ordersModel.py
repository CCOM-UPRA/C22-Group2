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