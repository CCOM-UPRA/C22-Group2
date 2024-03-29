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
    
# ------------------------------Address Methods------------------------------------
def getAddressModel(customer):
    db = DBConnect()
    sql = "SELECT * FROM shipping_address WHERE customer_id = %s"
    result = db.query(sql, (customer))
    print(result)
    return result

def editaddressmodel(address_line1, address_line2, city, state, zipcode,shipping_address_id):
    db = DBConnect()
    try:
        db.execute("UPDATE shipping_address SET address_line1 = %s, address_line2 = %s, "
                "city = %s, state = %s, zipcode = %s WHERE customer_id = %s AND shipping_address_id= %s",
                (address_line1, address_line2, city, state, zipcode, session['customer'], shipping_address_id))
        db.commit()

    except Exception as e:
        db.rollback()
        print(f"Error occurred: {e}")
        return None
    
def addaddressmodel(address_line1, address_line2, city, state, zipcode):
    db = DBConnect()
    try:
        db.execute("INSERT INTO shipping_address (address_line1, address_line2, city, state, zipcode, customer_id) VALUES ( %s, %s, %s, %s, %s, %s)",(address_line1, address_line2, city, state, zipcode, session['customer']))
        db.commit()

    except Exception as e:
        db.rollback()
        print(f"Error occurred: {e}")
        return None


# ------------------------------Payment Methods------------------------------------
def getPaymentModel(customer):
    db = DBConnect()
    sql = "SELECT * FROM payment_method WHERE customer_id = %s"
    result = db.query(sql, (customer))
    
    for payment in result:
        new_payment_num = '*'*(len(payment['card_number']) - 4)
        last_numbers = payment['card_number'][(len(payment['card_number']) - 4):len(payment['card_number'])]
        new_payment_num += last_numbers
        payment['placeholder_number'] = new_payment_num
    
    return result

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

