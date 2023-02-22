from backend_model.accountsModel import *
from flask import session
import os
import json

# This is a very basic dictionary with information for logging in
# Simulating our database
thisDict = {
    "email": "zulymar.garcia@upr.edu",
    "password": "pass1234",
    "user": "Zulymar"

}

def loginmodel(email, password):
    # Receive email and password to check in the "database"
    logins = getloginsmodel()
    if email in logins.keys():
        # User found! is password correct?
        if dict(logins.get(email)).get('password') == password:
            session['customer'] = dict(logins.get(email)).get('user')
            return "true"
    # No login lol
    return "false"

def addloginmodel(newUser : dict):
    addaccountmodel(newUser)

def getloginmodel(acc):
    getaccountmodel(acc)

# Get all accounts
def getloginsmodel():
    getaccountsmodel()

#print(getloginsmodel())