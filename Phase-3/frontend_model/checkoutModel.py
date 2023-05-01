from classes.db_connect import DBConnect
from flask import session
# Simulated tuple from customer database


def getUserModel(customer):
    db = DBConnect()
    sql = "SELECT * FROM customer NATURAL JOIN payment_method NATURAL JOIN shipping_address WHERE customer_id = %s"
    result = db.query(sql, (customer))
    return result[0]

