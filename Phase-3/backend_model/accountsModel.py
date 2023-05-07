from classes.db_connect import DBConnect
from passlib.hash import sha256_crypt
from flask import session
# import json
# from random import randrange

# usersPath = './UserData/users.json'
# adminsPath = './UserData/admins.json'

# Merge dictionaries
# def MagerDicts(dict1, dict2):
#     if isinstance(dict1, list) and isinstance(dict2, list):
#         return dict1 + dict2
#     elif isinstance(dict1, dict) and isinstance(dict2, dict):
#         return dict(list(dict1.items()) + list(dict2.items()))
#     return False

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
# In this case, we're requesting it via the key
def getaccountmodel(acc, userType):
    db = DBConnect()
    usersList = []
    if userType == 'customer':
        query = "SELECT * from customer join payment_method WHERE cistomer_id = %s"
        customerFound = db.query(query, acc)

        for user in customerFound:
            usersList.append({"id": user['customer_id'], "first_name": user['first_name'], "last_name": user['last_name'],
                          "email": user['email'], "aline1": user['bill_address_line1'], "aline2": user['bill_address_line2'],
                          "city": user['bill_city'], "state": user['bill_state'], "zipcode": user['bill_zipcode'],
                        "phone_number": user['phone_number'], "card_name": user["card_name"], "card_type": user['card_type'],
                        "card_number": user['card_number'], "exp_date": user['card_exp_date'], "status": user['status']})
    elif userType == 'administrator':
        query = "SELECT * from administrator WHERE administrator_id = %s"
        adminFound = db.query(query, acc)

        for user in adminFound:
            usersList.append(
                {"id": user['administrator_id'], "first_name": user['first_name'], "last_name": user['last_name'],
                 "email": user['email'], "phone_number": user['phone_number'],
                 "status": user['status']})
    return usersList
# Assigns key to account and adds to json
def addaccountmodel(acc : dict, admin = False):
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
def editaccountModel(userInfo, userType, id):
    db = DBconnect()
    usersList = []
    if userType == 'administrator':
        query = "UPDATE admin SET a_firstname = %s, a_lastname = %s, a_phone_number = %s, a_status = %s" \
                "WHERE admin_id = %s"
        db.execute(query, (userInfo[0], userInfo[1], userInfo[2], userInfo[3], id))
    elif userType == 'customer':
        query = "UPDATE customer SET c_first_name = %s, c_last_name = %s, address_line_1 = %s, address_line_2 = %s, " \
                "c_city = %s, c_state = %s, c_zipcode = %s, c_phone_number = %s, c_card_name = %s," \
                "c_card_type = %s, c_card_number = %s, c_exp_date = %s, c_status = %s WHERE c_id = %s"
        db.execute(query, (userInfo[0], userInfo[1], userInfo[2], userInfo[3], userInfo[4], userInfo[5], userInfo[6],
                           userInfo[7], userInfo[8], userInfo[9], userInfo[10], userInfo[11], userInfo[12], id))
    return

 
 # Pop account 
def deleteaccountmodel(acc : str, admin = False):
    path = adminsPath if admin else usersPath
    currentUsers = getaccountsmodel(admin=admin).pop(acc)
    # write to json
    with open(path, "w") as f:
        json.dump(currentUsers, f)
