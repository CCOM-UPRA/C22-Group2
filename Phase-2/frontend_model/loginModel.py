from classes.db_connect import DBConnect
from passlib.hash import sha256_crypt
from flask import session


def loginmodel(email : str, password : str):
    # Receive email and password to check in the "database"

    db = DBConnect()
    sql = "SELECT email, customer_id, password FROM customer WHERE email = %s"
    # Save user info in list
    userFound = db.query(sql, (email))
    # sha256_crypt.encrypt("password") = this is what is used to encrypt a password
    # sha256_crypt.verify(password_unhashed, password_hashed) = this is what is used to compare an unhashed and hashed password

    for u in userFound:
        if email == u['email'] and sha256_crypt.verify(password, u['password']) is True:
            session['customer'] = u['customer_id']
            # Create the session['customer'] saving the customer ID if user is found
            return "true"
        else:
            # If it didn't find user
            return "false"
             
def addloginmodel(first_name, last_name, email, password):
    db = DBConnect()
    
    sql = "SELECT 1 FROM customer WHERE email =  %s"
    exists = db.query(sql, (email))
    if exists:
        return "EXISTS"
    
    encrypted_password = sha256_crypt.encrypt(password)
    sql = "INSERT INTO customer (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
    db.execute(sql, (first_name, last_name, email, encrypted_password))
    
    # Get the new customer_id from the database. This also confirms that the record was made, otherwise customer_id will be NULL
    sql = "SELECT customer_id FROM customer WHERE email = %s"
    customer_id = db.query(sql, (email)).pop()['customer_id']
    
    sql = "INSERT INTO payment_method (customer_id) VALUES (%s)"
    db.execute(sql, (customer_id))

    sql = "INSERT INTO shipping_address (customer_id) VALUES (%s)"
    db.execute(sql, (customer_id))
    return "DONE"
    
def getloginmodel(acc):
    db = DBConnect()
    sql = "SELECT * FROM customer WHERE customer_id = %s"
    return db.query(sql, (acc))