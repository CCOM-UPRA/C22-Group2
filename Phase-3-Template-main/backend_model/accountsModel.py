from backend_model.connectDB import *

dictUser1 = {1: {'c_first_name': "Milena", 'c_last_name': "Ríos",
                'c_email': "milena.rios2@upr.edu", 'c_password': "aghetyeifc",
                'c_phone_number': 7871621782, 'c_status': 'active',
                'c_address_line_1': "Sector Barrios", 'c_address_line_2': "Calle 8 H20", 'c_city': "Hatillo", 'c_state': "Puerto Rico",
                 'c_zipcode': '00612', 'c_card_name': 'Milena Rios', 'c_card_type': 'Visa', 'c_exp_date': '2020-05-04',
                 'c_card_num': 1234123412341234}}

dictUser2 = {2: {'c_first_name': "Reina", 'c_last_name': "López",
                'c_email': "reina.lopez@upr.edu", 'c_password': "p1234567",
                'c_phone_number': 8981821728, 'c_status': 'active',
                'c_address_line_1': "Victor Azul", 'c_address_line_2': "Calle 9 A10", 'c_city': "Arecibo", 'c_state': "Puerto Rico",
                 'c_zipcode': '00610', 'c_card_name': 'Reina Lopez', 'c_card_type': 'Discover', 'c_exp_date': '2022-01-01',
                 'c_card_num': 1234123412341234}}

dictUser3 = {3: {'c_first_name': "Javier", 'c_last_name': "Quiñones",
                'c_email': "javier.quinones3@upr.edu", 'c_password': "pass1234",
                'c_phone_number': 7871231234, 'c_status': 'active',
                'c_address_line_1': "Vista Azulin", 'c_address_line_2': "Calle L11 L13", 'c_city': "Arecibor", 'c_state': "Puerto Ricor",
                 'c_zipcode': '00612', 'c_card_name': 'Javier Quiñones', 'c_card_type': 'Mastercard',
                 'c_exp_date': '2023-01-01', 'c_card_num': 1234123412341234}}


def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False


userList = dictUser1
userList = MagerDicts(userList, dictUser2)
userList = MagerDicts(userList, dictUser3)


# Get all accounts
def getaccountsmodel(userType):
    # DB credentials found in backend_model/connectDB.py
    db = Dbconnect()
    usersList = []

    if userType == 'admin':
        query = "SELECT * from admin"
        adminFound = db.select(query)

        for user in adminFound:
            usersList.append({"id": user['admin_id'], "first_name": user['a_firstname'], "last_name": user['a_lastname'],
                          "email": user['a_email'], "phone_number": user['a_phone_number'],
                          "status": user['a_status']})
    elif userType == 'customer':
        query = "SELECT * from customer"
        customerFound = db.select(query)

        for user in customerFound:
            usersList.append(
                {"id": user['c_id'], "first_name": user['c_first_name'], "last_name": user['c_last_name'],
                 "email": user['c_email'], "phone_number": user['c_phone_number'],
                 "status": user['c_status']})
    return usersList


# Get the specific account requested
# In this case, we're requesting it via the key
def getaccountmodel(acc, userType):
    db = Dbconnect()
    usersList = []
    if userType == 'customer':
        query = "SELECT * from customer WHERE c_id = %s"
        customerFound = db.select(query, acc)

        for user in customerFound:
            usersList.append({"id": user['c_id'], "first_name": user['c_first_name'], "last_name": user['c_last_name'],
                          "email": user['c_email'], "aline1": user['address_line_1'], "aline2": user['address_line_2'],
                          "city": user['c_city'], "state": user['c_state'], "zipcode": user['c_zipcode'],
                        "phone_number": user['c_phone_number'], "card_name": user["c_card_name"], "card_type": user['c_card_type'],
                        "card_number": user['c_card_number'], "exp_date": user['c_exp_date'], "status": user['c_status']})
    elif userType == 'admin':
        query = "SELECT * from admin WHERE admin_id = %s"
        adminFound = db.select(query, acc)

        for user in adminFound:
            usersList.append(
                {"id": user['admin_id'], "first_name": user['a_firstname'], "last_name": user['a_lastname'],
                 "email": user['a_email'], "phone_number": user['a_phone_number'],
                 "status": user['a_status']})
    return usersList


def updateAccountModel(userInfo, userType, id):
    db = Dbconnect()
    usersList = []
    if userType == 'admin':
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
