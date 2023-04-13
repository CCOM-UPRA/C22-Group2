from backend_model.accountsModel import *
from classes.db_connect import DBConnect
from passlib.hash import sha256_crypt
from flask import session


def loginmodel(email : str, password : str):
    # Receive email and password to check in the "database"

    db = DBConnect()
    user = []
    sql = "SELECT * from customer WHERE email = %s"
    userFound = db.query(sql, (email))

    # Save user info in list

    # sha256_crypt.encrypt("password") = this is what is used to encrypt a password
    # sha256_crypt.verify(password_unhashed, password_hashed) = this is what is used to compare an unhashed and hashed password

    for u in userFound:
        print("Hashed password from user: ", u['password'])
        if email == u['email'] and sha256_crypt.verify(password, u['password']) is True:
            session['customer'] = u['customer_id']
            # Create the session['customer'] saving the customer ID if user is found
            return "true"
        else:
            # If it didn't find user
            return "false"
    
    # logins = getaccountsmodel(admin=False)

    # for key, user in dict(logins).items():
    #         if dict(user).get('c_email') == email:
    #             if dict(user).get('c_password') == password:
    #                 session['customer'] = key
    #                 return "true"
    # return "false"
             
def addloginmodel(first_name, last_name, email, password):
    db = DBConnect()
    sql = "INSERT INTO customer (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
    db.execute(sql, (first_name, last_name, email, sha256_crypt.encrypt(password)))

def getloginmodel(acc):
    return getaccountmodel(acc, admin=False)

# Get all accounts
def getloginsmodel():
    return getaccountsmodel(admin=False)

#print(getloginsmodel())