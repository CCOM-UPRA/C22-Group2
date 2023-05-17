from frontend_model.profileModel import *

#access user

def getUser(customer):
    user = getUserModel(customer)
    
    return user

#edit profile info

def edit_profile(fname, lname, email):
    editprofilemodel(fname, lname, email)

#-------------------payment info-----------------------------
def edit_payment(card_name, card_type, card_exp_date, card_number, bill_address_line1 ,  bill_address_line2, bill_city, bill_state, bill_zipcode, payment_id):
    editpaymentmodel(card_name, card_type, card_exp_date, card_number, bill_address_line1 ,  bill_address_line2, bill_city, bill_state, bill_zipcode, payment_id)

def add_payment(card_name, card_type, card_exp_date, card_number, bill_address_line1 ,  bill_address_line2, bill_city, bill_state, bill_zipcode):
    addpaymentmodel(card_name, card_type, card_exp_date, card_number, bill_address_line1 ,  bill_address_line2, bill_city, bill_state, bill_zipcode)

def getPayment(customer):
    return getPaymentModel(customer)

#shipping ifo

def getAddress(customer):
    return getAddressModel(customer)

def edit_address(aline1, aline2, state, zipcode, city):
    editaddressmodel(aline1, aline2, state, zipcode, city)



# def edit_billaddress(aline1, aline2, state, zipcode, city):
#     edit_billaddressmodel(aline1, aline2, state, zipcode, city)
    
def edit_number(pnumber):
    editnumbermodel(pnumber)