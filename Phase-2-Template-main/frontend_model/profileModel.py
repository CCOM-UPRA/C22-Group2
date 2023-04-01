import pymysql
from flask import session


def getUserModel():
    user = []
    # Connect to DB using given credentials
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9602731',
                           user='sql9602731', password='zChRVJs2Nf', port=3306)
    cur = conn.cursor()
    # Find user via the customer ID saved in session
    cur.execute("SELECT * from customer WHERE c_id = %s", session['customer'])
    userFound = cur.fetchall()

    # Save tuple information in a list
    for users in userFound:
        user.append({"id": users[0], "name": users[1], "last_name": users[2], "address_line1": users[3],
                     "address_line2": users[4], "city": users[5], "state": users[6], "zipcode": users[7],
                     "email": users[8], "password": users[9], "phone_number": users[10], "card_name": users[11],
                     "card_type": users[12], "card_number": users[13], "exp_date": users[14], "status": users[15]})

    # To access user info:

        # for u in user:
        # u['id'], u['name'], u['email'], etc...
    return user


def editnumbermodel(number):
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9602731',
                           user='sql9602731', password='zChRVJs2Nf', port=3306)
    cur = conn.cursor()
    try:
        cur.execute("UPDATE customer SET c_phone_number = %s WHERE c_id = %s", (number, session['customer']))
        conn.commit()
        return 0

    except pymysql.Error as error:
        print(error)
        return 0

    else:
        cur.close()
        return 1


def editaddressmodel(aline1, aline2, state, zipcode, city):
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9602731',
                           user='sql9602731', password='zChRVJs2Nf', port=3306)
    cur = conn.cursor()
    try:
        cur.execute("UPDATE customer SET address_line_1 = %s, address_line_2 = %s, c_city = %s,"
                    "c_state = %s, c_zipcode = %s WHERE c_id = %s", (aline1, aline2, city, state, zipcode, session['customer']))
        conn.commit()
        return 0

    except pymysql.Error as error:
        print(error)
        return 0

    else:
        cur.close()
        return 1


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
