from classes.db_connect import DBConnect
from passlib.hash import sha256_crypt
from flask import session

# Get all accounts
def getaccountsmodel(userType):
    # DB credentials found in backend_model/connectDB.py
    db = DBConnect()
    usersList = []
    print(userType)

    if userType == 'administrator':
        query = "SELECT * FROM administrator"
        usersList = db.query(query)

    elif userType == 'customer':
        query = "SELECT * FROM customer"
        usersList = db.query(query)
    print(usersList)
    return usersList


# Get the specific account requested
def getaccountmodel(acc, userType):
    db = DBConnect()
    if userType == 'customer':
        query = "SELECT * FROM customer WHERE customer_id = %s"
        result = list(db.query(query, (acc))).pop()
        return result

    elif userType == 'administrator':
        query = "SELECT * FROM administrator WHERE administrator_id = %s"
        result = list(db.query(query, (acc))).pop()
        return result

# Creates new account and adds it to the database
def addaccountmodel(newAccount, userType):
    db = DBConnect()
    newAccount[3] = sha256_crypt.encrypt(newAccount[3])
    try:
        if userType == 'administrator':
            query = """INSERT INTO administrator (first_name, last_name, email,  password, phone_number, status) VALUES (%s, %s, %s, %s, %s, %s)"""
            db.execute(query, newAccount)
        elif userType == 'customer':
            query = """INSERT INTO customer (first_name, last_name, email,  password, phone_number, status) VALUES (%s, %s, %s, %s, %s, %s)"""
            db.execute(query, newAccount)

        db.commit()
    except Exception as e:
        # Log the error to console and rollback changes
        db.rollback()
        print(f"Error occurred: {e}")
        return None

    return


# Edits the user account
def updateAccountModel(userInfo, userType):
    db = DBConnect()

    try:
        if userType == 'administrator':
            query = """UPDATE administrator 
            SET first_name = %s, last_name = %s, phone_number = %s, email = %s, password = %s, status = %s
            WHERE administrator_id = %s"""
            db.execute(query, userInfo)
        elif userType == 'customer':
            query = """UPDATE customer 
            SET first_name = %s, last_name = %s, phone_number = %s, email = %s, password = %s, status = %s
            WHERE customer_id = %s"""
            # query = """UPDATE customer NATURAL JOIN shipping_address NATURAL JOIN payment_method
            # SET first_name = %s, last_name = %s, phone_number = %s, email = %s, password = %s, status = %s,
            #  address_line1 = %s, address_line2 = %s, city = %s, state = %s, zipcode = %s,
            #  card_name = %s, card_number = %s, card_type = %s, card_exp_date = %s
            # WHERE customer_id = %s"""
            db.execute(query, userInfo)

        db.commit()
    except Exception as e:
        # Log the error to console and rollback changes
        db.rollback()
        print(f"Error occurred: {e}")
        return None

    return
