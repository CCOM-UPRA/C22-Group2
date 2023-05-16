from backend_model.accountsModel import *


def getaccounts(userType):
    return getaccountsmodel(userType)

def getaccount(acc, userType):
    return getaccountmodel(acc, userType)

def addaccount(acc, userType):
    print("Account added")
    addaccountmodel(acc, admin)

def updateAccountcontroller(userInfo, userType):
    return updateAccountModel(userInfo, userType)

# def deleteaccount(acc : str, admin = False):
#     deleteaccountmodel(acc, admin=admin)