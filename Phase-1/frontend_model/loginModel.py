from flask import session
import os
import json
usersPath = os.getcwd() + '\\Phase-1\\logins.json'

# This is a very basic dictionary with information for logging in
# Simulating our database
thisDict = {
    "email": "zulymar.garcia@upr.edu",
    "password": "pass1234",
    "user": "Zulymar"

}

def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    print("Merge failed!")
    return False


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

    if email in thisDict.values() and password in thisDict.values():
        # If it found the email and pass in the dictionary
        session['customer'] = thisDict['user']
        # Create the session['customer']
        return "true"
    else:
        # If it didn't find user
        return "false"

def addloginmodel(newUser : dict):
    currentFile = getloginsmodel()
    currentFile = MagerDicts(currentFile, newUser)

    with open(usersPath, "w") as f:
        json.dump(currentFile, f)
    return currentFile

def getloginsmodel(acc):
    with open(usersPath, "r") as f:
        data = json.load(f)
    
    for key, user in dict(data).items():
        if key == acc:
            return user

# Get all accounts
def getloginsmodel():
    with open(usersPath, "r") as f:
        data = json.load(f)
    return dict(data)

#print(getloginsmodel())