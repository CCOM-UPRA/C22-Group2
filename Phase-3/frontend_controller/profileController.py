from frontend_model.profileModel import *

#access user

def getUser(customer):
    user = getUserModel(customer)
    
    return user

#edit profile info

def edit_profile(fname, lname, email):
    editprofilemodel(fname, lname, email)

#payment info
def edit_payment(name, c_type, number, exp_date):
    editpaymentmodel(name, c_type, number, exp_date)

def getPayment(customer):
    return getPaymentModel(customer)

#shipping ifo

def getAddress(customer):
    return getAddressModel(customer)

def edit_address(aline1, aline2, state, zipcode, city):
    editaddressmodel(aline1, aline2, state, zipcode, city)



def edit_billaddress(aline1, aline2, state, zipcode, city):
    edit_billaddressmodel(aline1, aline2, state, zipcode, city)
    
def edit_number(pnumber):
    editnumbermodel(pnumber)