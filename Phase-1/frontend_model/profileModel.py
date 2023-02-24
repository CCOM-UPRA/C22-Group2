# Simulated database of users
from backend_model.accountsModel import *

def getUserModel(customer):
    return getaccountmodel(customer, admin=False)