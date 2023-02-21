from frontend_model.loginModel import *
from flask import redirect, render_template


def logincontroller(email, password):
    result = loginmodel(email=email, password=password)
    # Check from loginModel's loginmodel() if user exists

    if 'checkout' in session:
        # If you're logging in from checking out
        session.pop('checkout', None)
        return redirect('/checkout')

    if result is "true":
        # If user exists, enter shop
        return redirect("/shop")
    else:
        # If user doesn't exist, return to login and trigger error message
        return redirect("/message")
