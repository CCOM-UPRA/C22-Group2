from backend_model.loginModel import *
from flask import redirect, render_template


def logincontroller(email, password):

    result = loginmodel(email=email, password=password)

    if result is "true":
        # If user exists, enter shop
        return redirect("/products")
    elif result is "deactivated":
        # If user doesn't exist, return to login and trigger error message
        return redirect("/login/deactivated")
    else:
        return redirect("/login/incorrect")