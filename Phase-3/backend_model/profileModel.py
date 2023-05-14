from classes.db_connect import DBConnect
from flask import session


def getUserModel(administrator):
    db = DBConnect()
    sql = "SELECT * FROM administrator WHERE administrator_id = %s"
    result = db.query(sql, (administrator)).pop()
    return result

