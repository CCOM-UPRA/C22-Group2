from frontend_model.profileModel import *
from backend_controller.accountsController import editaccountcontroller

def getUser(customer):
    return getUserModel(customer)

def changeinfo(acc, infolist):
    editaccountcontroller(acc, edits=infolist, admin=False)
