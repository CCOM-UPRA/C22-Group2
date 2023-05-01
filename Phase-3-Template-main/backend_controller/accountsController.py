from backend_model.accountsModel import *


def getaccounts(userType):
    return getaccountsmodel(userType)


def getaccount(acc, userType):
    return getaccountmodel(acc, userType)


def updateAccountController(userInfo, userType, id):
    return updateAccountModel(userInfo, userType, id)

