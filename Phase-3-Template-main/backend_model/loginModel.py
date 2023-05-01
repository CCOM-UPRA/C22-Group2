from flask import session
from backend_model.connectDB import *
import pymysql
from passlib.hash import sha256_crypt


def loginmodel(email, password):
    # DB credentials found in backend_model/connectDB.py
    db = Dbconnect()
    admin = []

    query = "SELECT * from admin WHERE a_email = %s"
    adminFound = db.select(query, email)

    for user in adminFound:
        admin.append({"id": user['admin_id'], "first_name": user['a_firstname'], "last_name": user['a_lastname'],
                      "email": user['a_email'], "password": user['a_password'], "phone_number": user['a_phone_number'],
                      "status": user['a_status']})

    if not admin:
        return "false"
    else:
        for u in admin:
            print("Admin info: ", admin)
            #print("Hashed password from user: ", u['password'])
            if email == u['email'] and sha256_crypt.verify(password, u['password']) is True:
                session['admin'] = u['id']
                # Create the session['admin'] saving the admin ID if user is found
                return "true"
            else:
                # If it didn't find user
                return "false"


