from frontend_model.profileModel import *


def getUser(customer):
    user = getUserModel(customer)
    
    return user

def changeinfo(acc, infolist):
    changeinfomodel(acc, infolist)

def edit_profile(fname, lname, email):
    editprofilemodel(fname, lname, email)

def edit_payment(name, c_type, number, exp_date):
    editpaymentmodel(name, c_type, number, exp_date)

def edit_address(aline1, aline2, state, zipcode, city):
    editaddressmodel(aline1, aline2, state, zipcode, city)
    
def edit_number(pnumber):
    editnumbermodel(pnumber)