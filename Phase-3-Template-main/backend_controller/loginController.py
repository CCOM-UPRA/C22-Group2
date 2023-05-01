from backend_model.loginModel import *
from flask import redirect, render_template


def logincontroller(email, password):

    result = loginmodel(email=email, password=password)
    print("Logging in...")

    if result is "true":
        print("Login successful!")
        return redirect("/products")
    else:
        print("Login failed ;-;")
        return redirect("/message")
