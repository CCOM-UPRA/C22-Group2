from flask import session
from backend_model.accountsModel import *

def loginmodel(email : str, password : str):
    # Receive email and password to check in the "database"
    logins = getaccountsmodel(admin=True)

    for key, admin in dict(logins).items():
            if dict(admin).get('c_email') == email:
                if dict(admin).get('c_password') == password:
                    session['admin'] = key
                    return "true"
    return "false"