# Simulated database of users
from backend_model.accountsModel import *
from backend_controller.accountsController import editaccountcontroller
def getUserModel(customer):
    return getaccountmodel(customer, admin=False)

def changeinfocontroller(acc, infolist):
    editaccountcontroller(acc, edits=infolist, admin=False)