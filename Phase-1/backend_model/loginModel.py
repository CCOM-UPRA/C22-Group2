from flask import session
from backend_controller.accountsController import *

# thisDict = {
#     "email": "eddy@gmail.com",
#     "password": "1234",
#     "user": "Eddy"
# }

# def loginmodel(email, password):
#     if email in thisDict.values() and password in thisDict.values():
#         session['admin'] = thisDict['user']
#         return "true"
#     else:
#         return "false"

def loginmodel(email : str, password : str):
    # Receive email and password to check in the "database"
    logins = getaccounts()

    for key, admin in dict(logins).items():
            if dict(admin).get('c_email') == email:
                if dict(admin).get('c_password') == password:
                    session['admin'] = key
                    return "true"
    return "false"