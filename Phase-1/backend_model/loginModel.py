from flask import session

thisDict = {
    "email": "eddy@gmail.com",
    "password": "1234",
    "user": "Eddy"
}


def loginmodel(email, password):
    if email in thisDict.values() and password in thisDict.values():
        session['admin'] = thisDict['user']
        return "true"
    else:
        return "false"
