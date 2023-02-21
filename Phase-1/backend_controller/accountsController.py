from backend_model.accountsModel import *


def getaccounts():
    return getaccountsmodel()


def getaccount(acc):
    return getaccountmodel(acc)

def addaccount(acc : dict):
    addaccountmodel(acc)