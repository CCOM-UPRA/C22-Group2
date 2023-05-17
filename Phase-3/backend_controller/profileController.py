from backend_model.profileModel import *

def getUser(administrator):
    user = getUserModel(administrator)
    return user


# -------------------- profile info--------------------

def edit_profile(fname, lname, email):
    editprofilemodel(fname, lname, email)


# --------------------Contact number----------------------

def edit_number(pnumber):
    editnumbermodel(pnumber)
