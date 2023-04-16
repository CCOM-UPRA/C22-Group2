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
    else:
        return render_template("404.html")


@app.route("/clear")
def clear():
    # Whenever you wish to log out or clear the session info, you can type /clear at the end of the Flask address
    session.clear()
    return redirect("/")


# Login page
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
        
        addloginmodel(fname, lname, email, pass1)
        logincontroller(email, pass1)
        return redirect('/shop')
    else:
        return redirect('/register/<message>')

@app.route("/shop", methods=['GET'])
def shop():
    # This is the shop's Flask portion
    # First we receive the list of products by accessing getProducts() from shopController
    if request.args.get('search_query'):
        products = searchProducts(request.args.get('search_query'))
    else:
        products = getProducts()

    # Then we create the shopping cart by accessing getCart in shopController
    getCart()

    # Find the different filter options for the products by accessing the functions from shopController
    sortings=getSortingPreference() 
    sortByOrder=getSortingByOrderPreference()

    locations = getLocation()
    plantType = getPlantType()
    sun = getSunExpo()
    watering = getWatering()

    # Set the amount of items user currently has in cart
    amount = 3
    # And set the amount for the entire site to access
    session['amount'] = amount
    total = 0
    # Set the cart's total amount for the page
    session['total'] = 0
    # And set the total for the entire site to access
    for item in session['cart']:
            total = float(item['price']) * float(item['quantity'])
            session['total'] += round(total,2)

    # Redirect to shop page with the variables used
    return render_template("shop-4column.html", products=products, amount=amount, sortings=sortings, sortByOrder=sortByOrder, plantType=plantType, locations=locations,
                           sun=sun, watering=watering, total=total)


@app.route("/profile")
def profile():
    # To open the user's profile page
    # Get user info from getUser() in profileController
    user = getUser(session['customer'])
    print(user)
    # Since I specified the variable as user1, that is how it will be called on the html page
    return render_template("profile.html", user1=user)


# make changes to profile info
@app.route("/editinfo", methods=["POST"])
def editinfo():
    if request.form.get('edit') == 'profile':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        edit_profile(fname=fname, lname=lname, email=email)
        
    elif request.form.get('edit') == 'payment':
        cname = request.form.get('cname')
        cnumber = request.form.get('cnumber')
        ctype = request.form.get('ctype')
        cdate = request.form.get('cdate')
        edit_payment(name=cname, c_type=ctype, number=cnumber, exp_date=cdate)
        
    elif request.form.get('edit') == 'address':
        aline1 = request.form.get('aline1')
        aline2 = request.form.get('aline2')
        state = request.form.get('state')
        city = request.form.get('city')
        zipcode = request.form.get('zipcode')
        edit_address(aline1, aline2, state, zipcode, city)
    
    elif request.form.get('edit') == 'bill_address':
        aline1 = request.form.get('billline1')
        aline2 = request.form.get('billline2')
        state = request.form.get('billstate')
        city = request.form.get('billcity')
        zipcode = request.form.get('billzipcode')
        edit_billaddress(aline1, aline2, state, zipcode, city)
    
    elif request.form.get('edit') == 'phone_number':
        pnumber = request.form.get('pnumber')
        edit_number(pnumber=pnumber)
            
    # Process register info here
    pass1 = request.form.get('pass1')
    
    # changeinfo(session['customer'], editAccount)
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
    # if request.form.get('submit') == 'add':

    product_id = request.form.get('p_id')
    quantity = request.form.get('quantity')
    addCartController(product_id, quantity)
    
    return redirect(request.referrer)


@app.route("/delete", methods=["POST"])
def delete():
    # > cartController. For purposes of this phase, the function doesn't work
    p_id = request.form.get("id")
    deleteCartItem(p_id)
    return redirect(request.referrer)


@app.route("/editcart", methods=["POST"])
def editcart():
    # edit cart here. not in function
    return redirect(request.referrer)


@app.route("/checkout", methods=["POST", "GET"])
def checkout():
    if request.form.get('edit') == 'profile':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        edit_profile(fname=fname, lname=lname, email=email)

    elif request.form.get('edit') == 'payment':
        cname = request.form.get('cname')
        cnumber = request.form.get('cnumber')
        ctype = request.form.get('ctype')
        cdate = request.form.get('cdate')
        edit_payment(name=cname, c_type=ctype, number=cnumber, exp_date=cdate)

    elif request.form.get('edit') == 'address':
        aline1 = request.form.get('aline1')
        aline2 = request.form.get('aline2')
        state = request.form.get('state')
        city = request.form.get('city')
        zipcode = request.form.get('zipcode')
        edit_address(aline1, aline2, state, zipcode, city)

    elif request.form.get('edit') == 'bill_address':
        aline1 = request.form.get('billline1')
        aline2 = request.form.get('billline2')
        state = request.form.get('billstate')
        city = request.form.get('billcity')
        zipcode = request.form.get('billzipcode')
        edit_billaddress(aline1, aline2, state, zipcode, city)

    elif request.form.get('edit') == 'phone_number':
        pnumber = request.form.get('pnumber')
        edit_number(pnumber=pnumber)
    # Check if customer is logged in
    if 'customer' in session:
        # > cartController
        user = getUserCheckout(session['customer'])
        total = session['total']

        # calculate total from the session cart
        # Reminder: session['cart'] was created in app.route(/shop)
        # The cart itself is found in cartModel
        return render_template("checkout.html", user1=user, total=total)

    else:
        # If customer isn't logged in, create session variable to tell us we're headed to checkout
        # Redirect us to login with message
        session['checkout'] = True
        return redirect("/wrong")


@app.route("/filter", methods=["POST", "GET"])
def filter():
    # filter happens here
    # not in function currently
    
    return redirect("/shop")


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
# sus