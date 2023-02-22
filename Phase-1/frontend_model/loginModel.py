from backend_controller.accountsController import *
from flask import session


def loginmodel(email : str, password : str):
    # Receive email and password to check in the "database"
    logins = getaccounts()

    for key, user in dict(logins).items():
            if dict(user).get('c_email') == email:
                if dict(user).get('c_password') == password:
                    session['customer'] = key
                    return "true"
    return "false"
             

def addloginmodel(newUser : dict):
    addaccount(newUser)

def getloginmodel(acc):
    getaccount(acc)

# Get all accounts
def getloginsmodel():
    getaccount()

#print(getloginsmodel())