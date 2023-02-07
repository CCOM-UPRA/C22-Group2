from flask import Flask, render_template, redirect, request, session
from frontend_controller.cartController import getCart, addCartController, deleteCartItem
from frontend_controller.checkoutController import getUserCheckout
from frontend_controller.invoiceController import getOrder, getOrderProducts
from frontend_controller.loginController import logincontroller
from frontend_controller.ordersController import getorder1, getorder2, getorder1products, getorder2products
from frontend_controller.profileController import getUser
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
    return render_template('login (2).html', message=message)


@app.route("/clear")
def clear():
    # Whenever you wish to log out or clear the session info, you can type /clear at the end of the Flask address
    session.clear()
    return redirect("/")


@app.route("/login", methods=['POST'])
def login():
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
    # Processs the register info
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    pass1 = request.form.get('pass1')
    pass2 = request.form.get('pass2')

    if pass1 == pass2:
        # Process register info here
        # Since it will not be functioning right now, let's simulate we registered with our usual login info:
        session['amount'] = 0
        email = 'javier.quinones3@upr.edu'
        passcode = 'pass1234'
        logincontroller(email=email, password=passcode)

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
    brands = getBrands()
    colors = getColors()
    videores = getVideoRes()
    wifi = getWifi()

    # Set the amount of items user currently has in cart
    amount = 3
    # And set the amount for the entire site to access
    session['amount'] = 3

    # Set the cart's total amount for the page
    total = 150.00
    # And set the total for the entire site to access
    session['total'] = 150.00

    # Redirect to shop page with the variables used
    return render_template("shop-4column.html", products=products, amount=amount, total=total, brands=brands,
                           colors=colors, videores=videores, wifi=wifi)


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
    # doesn't do anything at the moment
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


@app.route("/filter")
def filter():
    # filter happens here
    # not in function currently
    return redirect("/shop")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/