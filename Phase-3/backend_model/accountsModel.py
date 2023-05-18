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
    result = []
    if userType == 'customer':
        query = "SELECT * FROM customer WHERE customer_id = %s"
        
        result = list(db.query(query, (acc)))
    elif userType == 'administrator':
        query = "SELECT * FROM administrator WHERE administrator_id = %s"
        result = list(db.query(query, (acc)))
    
    if len(result) > 0:
        return result.pop()
    else:
        return []

# Creates new account and adds it to the database
def addaccountmodel(newAccount, userType):
    db = DBConnect()
    newAccount[3] = sha256_crypt.encrypt(newAccount[3])
    try:
        if userType == 'administrator' or userType == 'customer':
            query = "INSERT INTO "+userType+" (first_name, last_name, email,  password, phone_number, status) VALUES (%s, %s, %s, %s, %s, %s)"
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

    info = list(userInfo)

    try:
        if userType == 'administrator' or userType == 'customer':
            
            query = "UPDATE " + userType + \
            " SET first_name = %s, last_name = %s, phone_number = %s, email = %s, status = %s" \
            "WHERE " + userType + "_id = %s"
            
            # Remove password from info
            password = info.pop(4)
            db.execute(query, info)
            
            # Only update password when password
            if password != '':
                query = "UPDATE " + userType + \
                    " SET password = %s WHERE " + userType + "_id = %s"
                    
                params = (sha256_crypt.encrypt(password), info.pop())
                db.execute(query, params)


        db.commit()
    except Exception as e:
        # Log the error to console and rollback changes
        db.rollback()
        print(f"Error occurred: {e}")
        return None

    return
