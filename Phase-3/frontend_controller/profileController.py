from frontend_model.profileModel import *

#-------------------- user in session --------------------

def getUser(customer):
    user = getUserModel(customer)
    
    return user

#-------------------- profile info--------------------

def edit_profile(fname, lname, email):
    editprofilemodel(fname, lname, email)

#--------------------Contact number----------------------
    
def edit_number(pnumber):
    editnumbermodel(pnumber)

#-------------------payment info-----------------------------
def edit_payment(card_name, card_type, card_exp_date, card_number, bill_address_line1 ,  bill_address_line2, bill_city, bill_state, bill_zipcode, payment_id):
    editpaymentmodel(card_name, card_type, card_exp_date, card_number, bill_address_line1 ,  bill_address_line2, bill_city, bill_state, bill_zipcode, payment_id)

def add_payment(card_name, card_type, card_exp_date, card_number, bill_address_line1 ,  bill_address_line2, bill_city, bill_state, bill_zipcode):
    addpaymentmodel(card_name, card_type, card_exp_date, card_number, bill_address_line1 ,  bill_address_line2, bill_city, bill_state, bill_zipcode)

def getPayment(customer):
    return getPaymentModel(customer)

#----------------------shipping info------------------------------

def getAddress(customer):
    return getAddressModel(customer)

def edit_address(address_line1, address_line2, city, state, zipcode,shipping_address_id):
    editaddressmodel(address_line1, address_line2, city, state, zipcode,shipping_address_id)

def add_address(address_line1, address_line2, city, state, zipcode):
    addaddressmodel(address_line1, address_line2, city, state, zipcode)

