# Simulated database of users
from classes.db_connect import DBConnect
from flask import session

def getUserModel(customer):
    db = DBConnect()
    sql = "SELECT * FROM customer WHERE customer_id = %s"
    return db.query(sql, (customer))

# def changeinfomodel(acc, infolist):
#     editaccountmodel(acc, edits=infolist, admin=False)
    
def editnumbermodel(number):
    db = DBConnect()
    db.execute("UPDATE customer SET c_phone_number = %s WHERE c_id = %s", (number, session['customer']))


def editaddressmodel(aline1, aline2, state, zipcode, city):
    db = DBConnect()
    
    shipping_id = db.query("SELECT shipping_address_id FROM customer WHERE customer_id = %s", (session['customer']))
    if shipping_id:
        db.execute("UPDATE customer NATURAL JOIN shipping_address SET address_line1 = %s ,"
                   "address_line2 = %s , city = %s, state = %s, zipcode = %s WHERE customer_id = %s", (aline1, aline2, city, state, zipcode, session['customer']))
    else:
        # If the shipping_address doesn't exist, insert a new record and update the customer table with the new shipping_address_id
        db.execute("INSERT INTO shipping_address (address_line1, address_line2, city, state, zipcode) VALUES (%s, %s, %s, %s, %s)",
                   (aline1, aline2, city, state, zipcode))
    
    
    


def editpaymentmodel(name, c_type, number, exp_date):
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9602731',
                           user='sql9602731', password='zChRVJs2Nf', port=3306)
    cur = conn.cursor()
    try:
        cur.execute("UPDATE customer SET c_card_name = %s, c_card_number = %s, "
                    "c_card_type = %s, c_exp_date = %s WHERE c_id = %s",
                    (name, number, c_type, exp_date, session['customer']))
        conn.commit()
        return 0

    except pymysql.Error as error:
        print(error)
        return 0

    else:
        cur.close()
        return 1


def editprofilemodel(fname, lname, email):
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9602731',
                           user='sql9602731', password='zChRVJs2Nf', port=3306)
    cur = conn.cursor()
    try:
        cur.execute("UPDATE customer SET c_first_name = %s, c_last_name = %s, "
                    "c_email = %s WHERE c_id = %s",
                    (fname, lname, email, session['customer']))
        conn.commit()
        return 0

    except pymysql.Error as error:
        print(error)
        return 0

    else:
        cur.close()
        return 1