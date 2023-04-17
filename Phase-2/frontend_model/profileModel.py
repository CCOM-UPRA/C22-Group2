# Simulated database of users
from classes.db_connect import DBConnect
from flask import session

def getUserModel(customer):
    db = DBConnect()
    sql = "SELECT * FROM customer NATURAL JOIN payment_method NATURAL JOIN shipping_address WHERE customer_id = %s"
    result = db.query(sql, (customer)).pop()
    return result

# def changeinfomodel(acc, infolist):
#     editaccountmodel(acc, edits=infolist, admin=False)
    
def editnumbermodel(number):
    db = DBConnect()
    db.execute("UPDATE customer SET c_phone_number = %s WHERE c_id = %s", (number, session['customer']))

def editaddressmodel(aline1, aline2, state, zipcode, city):
    db = DBConnect()
    db.execute("UPDATE shipping_address SET address_line1 = %s, address_line2 = %s, "
                "city = %s, state = %s, zipcode = %s WHERE customer_id = %s",
                (aline1, aline2, city, state, zipcode, session['customer']))

def edit_billaddressmodel(aline1, aline2, state, zipcode, city):
    db = DBConnect()
    db.execute("UPDATE payment_method SET bill_address_line1 = %s, bill_address_line2 = %s, "
                "bill_city = %s, bill_state = %s, bill_zipcode = %s WHERE customer_id = %s",
                (aline1, aline2, city, state, zipcode, session['customer']))

def editpaymentmodel(name, c_type, number, exp_date):
    db = DBConnect()
    db.execute("UPDATE payment_method SET card_name = %s, card_number = %s, "
                "card_type = %s, card_exp_date = %s WHERE customer_id = %s",
                (name, number, c_type, exp_date, session['customer']))

def editprofilemodel(fname, lname, email):
    db = DBConnect()
    db.execute("UPDATE customer SET first_name = %s, last_name = %s, "
                    "email = %s WHERE customer_id = %s",
                    (fname, lname, email, session['customer']))

def editnumbermodel(pnumber):
    db = DBConnect()
    db.execute("UPDATE customer SET phone_number = %s"
                    "WHERE customer_id = %s",
                    (pnumber, session['customer']))