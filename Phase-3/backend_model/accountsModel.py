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
        query = "SELECT * FROM customer NATURAL JOIN payment_method NATURAL JOIN shipping_address WHERE customer_id = %s"
        result = db.query(query, (acc)).pop()
        return result

    elif userType == 'administrator':
        query = "SELECT * FROM administrator WHERE administrator_id = %s"
        result = db.query(query, (acc)).pop()
        return result

# Assigns key to account and adds to json
def addaccountmodel(acc, userType):
    path = adminsPath if admin else usersPath
    currentFile = getaccountsmodel(admin=admin)
    # assign new key to account
    newKey = randrange(0, 999999999)
    while(newKey in currentFile.keys()):
        newKey = randrange(0, 999999999)

    newEntry = {str(newKey):dict(acc)}
    # add account to dictionary
    currentFile = MagerDicts(currentFile, newEntry)
    # write to json
    with open(path, "w") as f:
        json.dump(currentFile, f)

# Edits the user account
def updateAccountModel(userInfo, userType):
    db = DBConnect()
    # usersList = []

    try:
        if userType == 'administrator':
            query = """UPDATE administrator 
            SET first_name = %s, last_name = %s, phone_number = %s, email = %s, password = %s, status = %s
            WHERE administrator_id = %s"""
            db.execute(query, userInfo)
        elif userType == 'customer':
            query = """UPDATE customer NATURAL JOIN shipping_address NATURAL JOIN payment_method 
            SET first_name = %s, last_name = %s, phone_number = %s, email = %s, password = %s, status = %s,
             address_line1 = %s, address_line2 = %s, city = %s, state = %s, zipcode = %s,
             card_name = %s, card_number = %s, card_type = %s, card_exp_date = %s
            WHERE customer_id = %s"""
            db.execute(query, userInfo)

        db.commit()
    except Exception as e:
        # Log the error to console and rollback changes
        db.rollback()
        print(f"Error occurred: {e}")
        return None

    return

 
 # Pop account 
# def deleteaccountmodel(acc : str, admin = False):
#     path = adminsPath if admin else usersPath
#     currentUsers = getaccountsmodel(admin=admin).pop(acc)
#     # write to json
#     with open(path, "w") as f:
#         json.dump(currentUsers, f)
