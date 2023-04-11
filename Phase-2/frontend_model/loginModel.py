from backend_model.accountsModel import *
from classes.db_connect import DBConnect
from flask import session


def loginmodel(email : str, password : str):
    # Receive email and password to check in the "database"

    db = DBConnect()
    logins = getaccountsmodel(admin=False)

    for key, user in dict(logins).items():
            if dict(user).get('c_email') == email:
                if dict(user).get('c_password') == password:
                    session['customer'] = key
                    return "true"
    return "false"
             

def addloginmodel(newUser : dict):
    addaccountmodel(newUser, admin=False)

def getloginmodel(acc):
    return getaccountmodel(acc, admin=False)

# Get all accounts
def getloginsmodel():
    return getaccountsmodel(admin=False)

#print(getloginsmodel())