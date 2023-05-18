from classes.db_connect import DBConnect
from flask import session


def getUserModel(administrator):
    db = DBConnect()
    sql = "SELECT * FROM administrator WHERE administrator_id = %s"
    result = db.query(sql, (administrator)).pop()
    return result


# Change info of profile
def editprofilemodel(fname, lname, email):
    db = DBConnect()
    try:
        db.execute("UPDATE administrator SET first_name = %s, last_name = %s, "
                   "email = %s WHERE administrator_id = %s",
                   (fname, lname, email, session['admin']))
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error occurred: {e}")
        return None


# Change contact number
def editnumbermodel(pnumber):
    db = DBConnect()
    try:
        db.execute("UPDATE administrator SET phone_number = %s"
                   "WHERE administrator_id = %s",
                   (pnumber, session['admin']))
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error occurred: {e}")
        return None
