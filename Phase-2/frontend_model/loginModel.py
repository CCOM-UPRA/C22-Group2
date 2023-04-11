from backend_model.accountsModel import *
from classes.db_connect import DBConnect
from flask import session


def loginmodel(email : str, password : str):
    # Receive email and password to check in the "database"

    db = DBConnect()
    user = []
    cur = db.cursor()
    cur.execute("SELECT * from customer WHERE c_email = %s", email)
    userFound = cur.fetchall()
    for users in userFound:
        user.append({"id": users[0], "name": users[1], "last_name": users[2], "address_line1": users[3],
                    "address_line2": users[4], "city": users[5], "state": users[6], "zipcode": users[7],
                    "email": users[8], "password": users[9], "phone_number": users[10], "card_name": users[11],
                    "card_type": users[12], "card_number": users[13], "exp_date": users[14], "status": users[15]})

    # Save user info in list

    # sha256_crypt.encrypt("password") = this is what is used to encrypt a password
    # sha256_crypt.verify(password_unhashed, password_hashed) = this is what is used to compare an unhashed and hashed password

    for u in user:
        print("Hashed password from user: ", u['password'])
        if email == u['email'] and sha256_crypt.verify(password, u['password']) is True:
            session['customer'] = u['id']
            # Create the session['customer'] saving the customer ID if user is found
            return "true"
        else:
            # If it didn't find user
            return "false"
    
    logins = getaccountsmodel(admin=False)

    for key, user in dict(logins).items():
            if dict(user).get('c_email') == email:
                if dict(user).get('c_password') == password:
                    session['customer'] = key
                    return "true"
    return "false"
             

def addloginmodel(newUser : dict):
    addaccountmodel(newUser, admin=False)

def getloginmodel(acc):
    return getaccountmodel(acc, admin=False)

# Get all accounts
def getloginsmodel():
    return getaccountsmodel(admin=False)

#print(getloginsmodel())