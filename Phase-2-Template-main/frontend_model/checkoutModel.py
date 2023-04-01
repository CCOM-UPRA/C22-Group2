import pymysql
from flask import session


def validateUserModel():
    user = []
    # Find user in DB according to customer ID saved in session
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9602731',
                           user='sql9602731', password='zChRVJs2Nf', port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * from customer WHERE c_id = %s", session['customer'])

    userFound = cur.fetchall()
    for users in userFound:
        user.append({"id": users[0], "name": users[1], "last_name": users[2], "address_line1": users[3],
                     "address_line2": users[4], "city": users[5], "state": users[6], "zipcode": users[7],
                     "email": users[8], "password": users[9], "phone_number": users[10], "card_name": users[11],
                     "card_type": users[12], "card_number": users[13], "exp_date": users[14], "status": users[15]})

    return user
