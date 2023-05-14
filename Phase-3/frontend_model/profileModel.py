# Simulated database of users
from classes.db_connect import DBConnect
from flask import session

def getUserModel(customer):
    db = DBConnect()
    #sql = "SELECT * FROM customer NATURAL JOIN payment_method NATURAL JOIN shipping_address WHERE customer_id = %s"
    sql = "SELECT * FROM customer WHERE customer_id = %s"
    result = db.query(sql, (customer)).pop()
    return result

#Change info of profile
def editprofilemodel(fname, lname, email):
    
    db = DBConnect()
    try:
        db.execute("UPDATE customer SET first_name = %s, last_name = %s, "
                    "email = %s WHERE customer_id = %s",
                    (fname, lname, email, session['customer']))
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error occurred: {e}")
        return None

#Change contact number
def editnumbermodel(pnumber):
    db = DBConnect()
    try:
        db.execute("UPDATE customer SET phone_number = %s"
                    "WHERE customer_id = %s",
                    (pnumber, session['customer']))
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error occurred: {e}")
        return None
    

def getAddressModel(customer):
    db = DBConnect()
    sql = "SELECT * FROM shipping_address WHERE customer_id = %s"
    result = db.query(sql, (customer))
    print(result)
    return result

def editaddressmodel(aline1, aline2, state, zipcode, city):
    db = DBConnect()
    db.execute("UPDATE shipping_address SET address_line1 = %s, address_line2 = %s, "
                "city = %s, state = %s, zipcode = %s WHERE customer_id = %s",
                (aline1, aline2, city, state, zipcode, session['customer']))
    

def getPaymentModel(customer):
    db = DBConnect()
    sql = "SELECT * FROM payment_method WHERE customer_id = %s"
    result = db.query(sql, (customer))
    print(result)
    return result

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


