from frontend_model.profileModel import *


def getUser(customer):
    return getUserModel(customer)

def changeinfo(acc, infolist):
    changeinfomodel(acc, infolist)

def editpayment(name, c_type, number, exp_date):
    editpaymentmodel(name, c_type, number, exp_date)