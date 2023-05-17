#  database of users
from classes.db_connect import DBConnect
from flask import session

#User in session
def getUserModel(customer):
    db = DBConnect()
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
    
#S
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

# def edit_billaddressmodel(aline1, aline2, state, zipcode, city):
#     db = DBConnect()
#     db.execute("UPDATE payment_method SET bill_address_line1 = %s, bill_address_line2 = %s, "
#                 "bill_city = %s, bill_state = %s, bill_zipcode = %s WHERE customer_id = %s",
#                 (aline1, aline2, city, state, zipcode, session['customer']))

def editpaymentmodel(card_name, card_type, card_exp_date, card_number, bill_address_line1 ,  bill_address_line2, bill_city, bill_state, bill_zipcode, payment_id):
    db = DBConnect()
    try:
        db.execute("UPDATE payment_method SET card_name = %s, card_type = %s, "
                "card_exp_date = %s, card_number = %s, bill_address_line1 = %s, bill_address_line2 = %s, "
                "bill_city = %s, bill_state = %s, bill_zipcode = %s WHERE customer_id = %s AND payment_id = %s",
                (card_name, card_type, card_exp_date, card_number, bill_address_line1 ,  bill_address_line2, bill_city, bill_state, bill_zipcode, session['customer'],payment_id))
        db.commit()

    except Exception as e:
        db.rollback()
        print(f"Error occurred: {e}")
        return None

def addpaymentmodel(card_name, card_type, card_exp_date, card_number, bill_address_line1 ,  bill_address_line2, bill_city, bill_state, bill_zipcode):
    db = DBConnect()
    try:
        db.execute("INSERT INTO payment_method (card_name, card_type, card_exp_date, card_number, bill_address_line1 ,  bill_address_line2, bill_city, bill_state, bill_zipcode, customer_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(card_name, card_type, card_exp_date, card_number, bill_address_line1 ,  bill_address_line2, bill_city, bill_state, bill_zipcode, session['customer']))
        db.commit()

    except Exception as e:
        db.rollback()
        print(f"Error occurred: {e}")
        return None

