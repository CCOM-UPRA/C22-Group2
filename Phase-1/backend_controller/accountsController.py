from backend_model.accountsModel import *


def getaccounts(admin = True):
    return getaccountsmodel(admin)

def getaccount(acc, admin=True):
    return getaccountmodel(acc, admin)

def addaccount(acc : dict, admin=True):
    print("Account added")
    addaccountmodel(acc, admin)

def editaccount(acc, edits : dict, admin=True):
    editaccountmodel(acc, edits, admin=admin)