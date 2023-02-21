from backend_model.loginModel import *
from flask import redirect, render_template


def logincontroller(email, password):
    # print("hi2")
    result = loginmodel(email=email, password=password)
    print("testing login")
    if result is "true":
        print("login true")
        return redirect("/products") #TODO añadir links en products.html
    else:
        print("login false")
        return redirect("/message")
