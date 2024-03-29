from flask import Flask, redirect, render_template, request, session, url_for
from frontend_controller.cartController import (addCartController,
                                                deleteCartItem, getCart)
from frontend_controller.checkoutController import getUserCheckout
from frontend_controller.invoiceController import *
from frontend_controller.loginController import *
from frontend_controller.ordersController import getorder, get_orders_and_products, cancelOrder
from frontend_controller.profileController import *
from frontend_controller.shopController import *

app = Flask(__name__, template_folder='frontend/')
app.secret_key = 'akeythatissecret'

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
        
        result = addloginmodel(fname, lname, email, pass1)
        
        if result == "EXISTS":
            return redirect("/register/emailused")
            
        logincontroller(email, pass1)
        return redirect('/shop')
    else:
        return redirect('/register/passwordnotmatched')


@app.route("/shop", methods=['GET'])
def shop():
    # This is the shop's Flask portion
    # First we receive the list of products by accessing getProducts() from shopController
        
    search_query = request.args.get('search_query')
    flocations = request.args.getlist('locations')
    fplantType = request.args.getlist('plant-types')
    fsunExp = request.args.getlist('sun-exps')
    fwatering = request.args.getlist('waterings')
    fsorting=request.args.getlist('sortings')
    forderBy=request.args.getlist('sorting-order')
    print("The search query is: ", search_query)
    products = get_filtered_products(locations=flocations, plantType=fplantType,sun=fsunExp,
                                     watering=fwatering, sortByOrder=forderBy, sortings=fsorting, search_query=search_query)

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
    amount = 0
    # And set the amount for the entire site to access
    session['amount'] = amount
    total = 0
    # Set the cart's total amount for the page
    session['total'] = 0
    # And set the total for the entire site to access
    for item in session['cart']:
            total += float(item['price']) * float(item['product_quantity'])
            amount += 1 * int(item['product_quantity'])

    session['total'] = f'{total:.2f}'
    session['amount'] = amount
    
    # Replace 
    for product in products:
        for item in session['cart']:
            if item['product_id'] == product['product_id']:
                product['default_quantity'] = item['product_quantity']
                print("The default quantity: ", product['default_quantity'])
            else:
                product['default_quantity'] = 1

    # Redirect to shop page with the variables used
    return render_template("shop-4column.html", products=products, amount=amount, sortings=sortings, sortByOrder=sortByOrder, plantType=plantType, locations=locations,
                           sun=sun, watering=watering, total=total, search_query=search_query)


@app.route("/profile")
def profile():
    # To open the user's profile page
    # Get user info from getUser() in profileController
    user = getUser(session['customer'])
    shipping_addresses = getAddress(session['customer'])
    payment_methods = getPayment(session['customer'])

    print(user)
    # Since I specified the variable as user1, that is how it will be called on the html page
    return render_template("profile.html", user1=user, shipping_addresses=shipping_addresses, payment_methods=payment_methods)


# make changes to profile info
@app.route("/editinfo", methods=["POST"])
def editinfo():
    #------------Your profile--------------
    if request.form.get('edit') == 'profile':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        edit_profile(fname=fname, lname=lname, email=email)

    #------------Contact Number--------------
    elif request.form.get('edit') == 'phone_number':
        pnumber = request.form.get('pnumber')
        edit_number(pnumber=pnumber)
        
   #------------Shipping-------------------------
    elif request.form.get('edit') == 'shipping_address-add':
        address_line1 = request.form.get('aline1')
        address_line2 = request.form.get('aline2')
        city = request.form.get('city')
        state = request.form.get('state')
        zipcode = request.form.get('zipcode')
        
        add_address(address_line1, address_line2, city, state, zipcode)


    elif request.form.get('edit') == 'shipping_address':
        address_line1 = request.form.get('aline1')
        address_line2 = request.form.get('aline2')
        city = request.form.get('city')
        state = request.form.get('state')
        zipcode = request.form.get('zipcode')
        shipping_address_id = request.form.get('shipping_address_id')
        edit_address(address_line1, address_line2, city, state, zipcode,shipping_address_id)

        #------------Payment----------------------
    
    elif request.form.get('edit') == 'payment_method-add':
        cname = request.form.get('cname')
        cnumber = request.form.get('cnumber')
        ctype = request.form.get('ctype')
        cdate = request.form.get('cdate')
        aline1 = request.form.get('aline1')
        aline2 = request.form.get('aline2')
        state = request.form.get('state')
        city = request.form.get('city')
        zipcode = request.form.get('zipcode')
        
        add_payment(card_name=cname, card_type=ctype, card_exp_date=cdate, card_number=cnumber, bill_address_line1=aline1 ,  bill_address_line2=aline2, bill_city=city, bill_state=state, bill_zipcode=zipcode)
    
    elif request.form.get('edit') == 'payment':
        cname = request.form.get('cname')
        cnumber = request.form.get('cnumber')
        ctype = request.form.get('ctype')
        cdate = request.form.get('cdate')
        aline1 = request.form.get('aline1')
        aline2 = request.form.get('aline2')
        state = request.form.get('state')
        city = request.form.get('city')
        zipcode = request.form.get('zipcode')
        payment_id = request.form.get('payment_id')
        edit_payment(card_name=cname, card_type=ctype, card_exp_date=cdate, card_number=cnumber, bill_address_line1=aline1 ,  bill_address_line2=aline2, bill_city=city, bill_state=state, bill_zipcode=zipcode, payment_id=payment_id)
            
    # Process register info here
    #  pass1 = request.form.get('pass1')
    
    # changeinfo(session['customer'], editAccount)
    return redirect(request.referrer)
    
    
@app.route("/password", methods=["POST"])
def password():
    # make password changes
    # optional portion for students to implement or not
    return render_template("change-password.html")


@app.route("/orders")
def orders():
    # Redirects us to the orders list page of the user
    # Fetches each order and its products from ordersController
    
    orders = get_orders_and_products(session['customer'])

    return render_template("orderlist.html", orders=orders)


@app.route("/addcart", methods=["POST"])
def addcart():

    product_id = request.form.get('p_id')
    quantity = int(request.form.get('quantity'))
    addCartController(product_id, quantity)
    
    return redirect(request.referrer)


@app.route("/delete", methods=["POST"])
def delete():
    
    p_id = request.form.get("id")
    deleteCartItem(p_id)

    amount = 0
    total = 0
    session['amount'] = 0
    session['total'] = 0
    
    for item in session['cart']:
            total += float(item['price']) * float(item['product_quantity'])
            amount += 1 * int(item['product_quantity'])
            
    session['total'] = f'{total:.2f}'
    session['amount'] = amount

    return redirect(request.referrer)


@app.route("/editcart", methods=["POST"])
def editcart():
    # edit cart here. not in function
    p_id = request.form.get('p_id')
    quantity = int(request.form.get('quantity'))
    
    if 'cart' in session:
        for product in session['cart']:
            if int(product['product_id']) == int(p_id):
                if int(quantity) == 0:
                    deleteCartItem(int(p_id))
                else:
                    product['product_quantity'] = int(quantity)

    total = 0
    amount = 0
    for item in session['cart']:
            total += float(item['price']) * float(item['product_quantity'])
            amount += 1 * int(item['product_quantity'])
            item['total_price'] = round(int(item['product_quantity']) * float(item['price']),2)

    session['total'] = f'{total:.2f}'
    session['amount'] = amount

    return redirect(request.referrer)


@app.route("/checkout")
def checkout():
    # Check if customer is logged in
    if 'customer' in session:
        # > cartController
        user = getUserCheckout(session['customer'])
        total = session['total']
        shipping_addresses = getAddress(session['customer'])
        payment_methods = getPayment(session['customer'])

        # calculate total from the session cart
        # Reminder: session['cart'] was created in app.route(/shop)
        # The cart itself is found in cartModel
        return render_template("checkout.html", user1=user, total=total, shipping_addresses=shipping_addresses, payment_methods=payment_methods)

    else:
        # If customer isn't logged in, create session variable to tell us we're headed to checkout
        # Redirect us to login with message
        session['checkout'] = True
        return redirect("/wrong")


@app.route("/editcheckout", methods=["POST"])
def editcheckout():
    
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

    elif request.form.get('edit') == 'phone_number':
        pnumber = request.form.get('pnumber')
        edit_number(pnumber=pnumber)
        
    return redirect("/checkout")


@app.route("/createorder", methods=['POST'])
def createorder():
    shipping_address = request.form.get('shipping_address')
    payment_method = request.form.get('payment_method')
    order_id = addOrder(shipping_address, payment_method)
    
    return redirect(url_for("invoice", order_id=order_id))


@app.route("/cancelorder/<order_id>")
def cancelorder(order_id):
    
    cancelOrder(order_id)
    
    return redirect(request.referrer)


@app.route("/invoice/<order_id>")
def invoice(order_id):
    
    if order_id:
        order = getOrder(order_id)
        products = getOrderProducts(order_id)
    else:
        order = []
        products = []
    # Total amount of items in this order:
    amount = 0
    for product in products:
        amount += product['product_quantity']

    if len(order) == 0:
        return render_template('404.html')
    else:
        return render_template("invoice.html", order=order, products=products, amount=amount)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/