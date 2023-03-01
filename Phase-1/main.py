from flask import Flask, render_template, redirect, request, session
from frontend_controller.cartController import getCart, addCartController, deleteCartItem
from frontend_controller.checkoutController import getUserCheckout
from frontend_controller.invoiceController import getOrder, getOrderProducts
from frontend_controller.loginController import *
from frontend_controller.ordersController import getorder1, getorder2, getorder1products, getorder2products
from frontend_controller.profileController import *
from frontend_controller.shopController import *

app = Flask(__name__, template_folder='frontend/')
app.secret_key = 'akeythatissecret'

# In this template, you will usually find functions with comments tying them to a specific controller
# main.py accesses the frontend folders
# Every controller accesses its relevant model and will send the information back to this Flask app

# Redirects us here if no url is given
@app.route("/", defaults={'message': None})
# Or if any url other than the ones set in this Flask application is provided, making it a <message>
@app.route("/<message>")
def enterpage(message):
    # This is the very page you enter when booting up Flask. You will be redirected to the login page.
    if (message == None or message == "index.html"):
        return shop()

@app.route("/filter", methods=["POST", "GET"])
def filter():
    # filter happens here
    # not in function currently
    
    return redirect("/shop")

@app.route("/clear")
def clear():
    # Whenever you wish to log out or clear the session info, you can type /clear at the end of the Flask address
    session.clear()
    return redirect("/")

@app.route("/login")
@app.route("/login/<message>")
def login(message = None):
    return render_template('login (2).html', message=message)

@app.route("/attemptlogin", methods=['POST'])
def attemptlogin():
    # Enters here when logging in
    email = request.form.get('email')
    passcode = request.form.get('password')
    session['amount'] = 0
    # Receive your login information and send to the loginController's logincontroller()
    return logincontroller(email=email, password=passcode)


@app.route("/register/", defaults={'message': None})
@app.route('/register/<message>')
def register(message):
    # Redirects to register page
    return render_template('register.html', message=message)


@app.route("/registerinfo", methods=['POST'])
def registerinfo():
    # Process the register info
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    pass1 = request.form.get('pass1')
    pass2 = request.form.get('pass2')

    if pass1 == pass2:
        # Process register info here
        session['amount'] = 0
        
        newAccount = {
            "c_first_name": fname,
            "c_last_name": lname,
            "c_email": email,
            "c_password": pass1,
            "c_phone_number": "9999999999",
            "c_status": "Active",
            "c_address_line_1": "Street num 1",
            "c_address_line_2": "",
            "c_city": "San Juan",
            "c_state": "Puerto Rico",
            "c_zipcode": "0000",
            "c_card_name": "",
            "c_card_type": "",
            "c_exp_date": "",
            "c_card_num": ""
            }
        
        addloginmodel(newAccount)
        logincontroller(email, pass1)
        return redirect('/shop')
    else:
        return redirect('/register/<message>')


@app.route("/shop")
def shop():
    # This is the shop's Flask portion
    # First we receive the list of products by accessing getProducts() from shopController
    products = getProducts()

    # Then we create the shopping cart by accessing getCart in shopController
    getCart()

    # Find the different filter options for the products by accessing the functions from shopController
    locations = getLocation()
    family = getFamilyType()
    sun = getSunExpo()
    watering = getWatering()

    # Set the amount of items user currently has in cart
    amount = 3
    # And set the amount for the entire site to access
    session['amount'] = amount

    # Set the cart's total amount for the page
    total = 56.97
    # And set the total for the entire site to access
    session['total'] = total

    # Redirect to shop page with the variables used
    return render_template("shop-4column.html", products=products, amount=amount, family=family, locations=locations,
                           sun=sun, watering=watering, total=total)


@app.route("/profile")
def profile():
    # To open the user's profile page
    # Get user info from getUser() in profileController
    user = getUser(session['customer'])

    # Since I specified the variable as user1, that is how it will be called on the html page
    return render_template("profile.html", user1=user)


@app.route("/editinfo", methods=["POST"])
def editinfo():
    # make changes to profile info
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    pnumber = request.form.get('pnumber')
    email = request.form.get('email')
    pass1 = request.form.get('pass1')
    aline1 = request.form.get('aline1')
    aline2 = request.form.get('aline2')
    city = request.form.get('city')
    state = request.form.get('state')
    zipcode = request.form.get('zipcode')
    cname = request.form.get('cname')
    cnumber = request.form.get('cnumber')
    ctype = request.form.get('ctype')
    cdate = request.form.get('cdate')
        # Process register info here
        
    editAccount = {
        "c_first_name": fname,
        "c_last_name": lname,
        "c_email": email,
        "c_password": pass1,
        "c_phone_number": pnumber,
        "c_status": "Active",
        "c_address_line_1": aline1,
        "c_address_line_2": aline2,
        "c_city": city,
        "c_state": state,
        "c_zipcode": zipcode,
        "c_card_name": cname,
        "c_card_type": ctype,
        "c_exp_date": cdate,
        "c_card_num": cnumber
        }

    changeinfo(session['customer'], editAccount)
    return redirect("/profile")


@app.route("/password", methods=["POST"])
def password():
    # make password changes
    # optional portion for students to implement or not
    return render_template("change-password.html")


@app.route("/orders")
def orders():
    # Redirects us to the orders list page of the user
    # Fetches each order and its products from ordersController
    order1 = getorder1()
    products1 = getorder1products()
    order2 = getorder2()
    products2 = getorder2products()

    return render_template("orderlist.html", order1=order1, products1=products1, order2=order2, products2=products2)


@app.route("/addcart", methods=["POST"])
def addcart():
    # > cartController. For purposes of this phase, the function doesn't work
    addCartController()
    # request.referrer means you will be redirected to the current page you were in
    return redirect(request.referrer)


@app.route("/delete")
def delete():
    # > cartController. For purposes of this phase, the function doesn't work
    deleteCartItem()
    return redirect(request.referrer)


@app.route("/editcart", methods=["POST"])
def editcart():
    # edit cart here. not in function
    return redirect(request.referrer)


@app.route("/checkout")
def checkout():
    # Check if customer is logged in
    if 'customer' in session:
        # > cartController
        user = getUserCheckout()
        total = 0

        # calculate total from the session cart
        # Reminder: session['cart'] was created in app.route(/shop)
        # The cart itself is found in cartModel
        for key, item in session['cart'].items():
            total += item['total_price']
        return render_template("checkout.html", user1=user, total=total)

    else:
        # If customer isn't logged in, create session variable to tell us we're headed to checkout
        # Redirect us to login with message
        session['checkout'] = True
        return redirect("/wrong")


@app.route("/invoice")
def invoice():
    # > invoiceController
    order = getOrder()
    products = getOrderProducts()
    # Total amount of items in this simulated order:
    amount = 3
    return render_template("invoice.html", order=order, products=products, amount=amount)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/