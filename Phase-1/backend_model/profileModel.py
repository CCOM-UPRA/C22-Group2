from backend_model.accountsModel import *

def getUserModel(customer):
    users = getaccountsmodel()
    for key, user in users.items():
        if customer == user['c_first_name']:
            return user

