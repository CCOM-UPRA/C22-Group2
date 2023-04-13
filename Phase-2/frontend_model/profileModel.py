# Simulated database of users
from classes.db_connect import DBConnect
from flask import session

def getUserModel(customer):
    db = DBConnect()
    sql = "SELECT * FROM customer WHERE customer_id = %s"
    result = db.query(sql, (customer))
    return result

# def changeinfomodel(acc, infolist):
#     editaccountmodel(acc, edits=infolist, admin=False)
    
def editnumbermodel(number):
    db = DBConnect()
    db.execute("UPDATE customer SET c_phone_number = %s WHERE c_id = %s", (number, session['customer']))

def editaddressmodel(aline1, aline2, state, zipcode, city):
    db = DBConnect()
    
def editpaymentmodel(name, c_type, number, exp_date):
    db = DBConnect()
    db.execute("UPDATE customer SET card_name = %s, card_number = %s, "
                "card_type = %s, card_exp_date = %s WHERE customer_id = %s",
                (name, number, c_type, exp_date, session['customer']))

def editprofilemodel(fname, lname, email):
    db = DBConnect()
    db.execute("UPDATE customer SET first_name = %s, last_name = %s, "
                    "email = %s WHERE customer_id = %s",
                    (fname, lname, email, session['customer']))