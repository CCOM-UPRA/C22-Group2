from backend_model.accountsModel import *


def getaccounts(userType):
    return getaccountsmodel(userType)

def getaccount(acc, userType):
    return getaccountmodel(acc, userType)

def addaccount(acc : dict, admin=True):
    print("Account added")
    addaccountmodel(acc, admin)

def editaccountcontroller(userInfo, userType, id):
    return editaccountModel(userInfo, userType, id)

def deleteaccount(acc : str, admin = False):
    deleteaccountmodel(acc, admin=admin)