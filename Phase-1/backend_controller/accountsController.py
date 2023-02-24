from backend_model.accountsModel import *


def getaccounts():
    return getaccountsmodel(admin=True)

def getaccount(acc):
    return getaccountmodel(acc, admin=True)

def addaccount(acc : dict):
    addaccountmodel(acc, admin=True)