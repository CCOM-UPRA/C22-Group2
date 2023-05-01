from passlib.handlers.sha2_crypt import sha256_crypt
import pymysql
from flask import session
from backend_model.connectDB import *


def changePass():
    admin = []

    # DB credentials found in backend_model/connectDB.py
    db = Dbconnect()

    query = "SELECT * from admin WHERE a_email = %s "
    email = 'javier@dragonflydrones.com'

    adminFound = db.select(query, email)
    print(adminFound)
    # Select the specific admin whose password you want to hash via the email

    # This part isn't necessary here but is shown so student can visualize the DB structure
    for user in adminFound:
        admin.append({"id": user['admin_id'], "first_name": user['a_firstname'], "last_name": user['a_lastname'],
                      "email": user['a_email'], "password": user['a_password'], "phone_number": user['a_phone_number'],
                      "status": user['a_status']})
        # Save the user's password in 'passw'
        passw = user['a_password']

    # Encrypt the password using the sha256_crypt function
    hashpass = sha256_crypt.encrypt(passw)
    print("Hashed password: ", hashpass)

    try:
        # Once encrypted, save this new hashed password to DB
        query = "UPDATE admin SET a_password = %s WHERE a_email = %s "
        db.execute(query, (hashpass, email))
        return 1

    except pymysql.Error as error:
        print(error)
        return 0

