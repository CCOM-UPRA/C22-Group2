from flask import session
from backend_model.accountsModel import *

def loginmodel(email : str, password : str):
    # Receive email and password to check in the "database"

    db = DBConnect()
    sql = "SELECT email, administrator_id, password FROM administrator WHERE email = %s AND status = 1"
    # Save user info in list
    userFound = db.query(sql, (email))
    # sha256_crypt.encrypt("password") = this is what is used to encrypt a password
    # sha256_crypt.verify(password_unhashed, password_hashed) = this is what is used to compare an unhashed and hashed password

    for u in userFound:
        if email == u['email'] and sha256_crypt.verify(password, u['password']) is True:
            session['admin'] = u['administrator_id']
            # Create the session['customer'] saving the customer ID if user is found
            return "true"
        else:
            # If it didn't find user
            return "false"