import os
from functools import wraps #TODO check
from datetime import datetime, timedelta
from time import strftime

from flask import Flask, render_template, redirect, request, session, url_for
from werkzeug.utils import secure_filename

from backend_controller.loginController import *
from backend_controller.ordersController import ordersController, getorder, getorderproducts
from backend_controller.productsController import *
from backend_controller.accountsController import *
from backend_controller.reportsController import getDatedReportDay, getDatedReportWeek, getStockReport
from backend_controller.profileController import *

# In this template, you will usually find functions with comments tying them to a specific controller
# main.py accesses the frontend folders
# Every controller accesses its relevant model and will send the information back to this Flask app

app = Flask(__name__, template_folder='backend/')
app.secret_key = 'akeythatissecret'


# Checks if user is logged in before entering page
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('admin'):
            return f(*args, **kwargs)      
        return redirect('/login')
    return decorated_function

@app.route("/", defaults={'message': None})
@app.route("/<message>")
def enterpage(message):
    # Defaults to product page if logged in
    if session.get('admin'):
        return redirect("/products")
    return redirect("/login")
    

@app.route("/clear")
def clear():
    # Clear session information
    
    session.clear()
    return redirect("/")

@app.route("/hashpass")
def hashpass():
    # For hashing already established unhashed passwords
    # changePassController ->
    changePass()
    return redirect("/")

@app.route("/login")
@app.route("/login/<message>")
def login(message = None):
    return render_template('login (2).html', message=message)

@app.route("/attemptlogin", methods=['POST'])
def attemptlogin():
    email = request.form.get('email')
    password = request.form.get('password')
    session['amount'] = 0
    # POINTER: loginModel creates a session['admin'] instead
    # Always advisable to name your frontend and backend sessions differently to not cause errors via lingering sessions
    return logincontroller(email=email, password=password)

@app.route("/profile")
@login_required
def profile():
    admin = getUser(session['admin'])
    return render_template("profile.html", user1=admin)


@app.route("/password", methods=["POST"])
@login_required
def password():
    # make password changes
    # optional for students to implement or not
    return render_template("change-password.html")


@app.route("/products")
@login_required
def products():
    productsp = getProducts()
    return render_template("products.html", products=productsp)


@app.route("/product/<prod>")
@login_required
def product(prod):
    return redirect(url_for('single_product', prodID=prod))


@app.route("/single_product/<prodID>")
@login_required
def single_product(prodID):
    # Return product page for single product selected
    product = getsingleproduct(prodID)
    print("The product: ", product)
    return render_template("single_product.html", prod=product)


@app.route("/editproduct", methods=['POST'])
@login_required
def editproduct():
    # process the changes to a product's information
    print("Edit product called")
    name = request.form.get('name')
    location = request.form.get('location')
    family = request.form.get('family')
    sun = request.form.get('sun')
    water = request.form.get('water')
    img = request.form.get('img')
    price = request.form.get('price')
    stock = request.form.get('stock')
    desc = request.form.get('desc')

    newProduct = {
    "name": name,
    "location": location,
    "family type": family,
    "sun": sun,
    "water": water,
    "img": img,
    "price": price,
    "stock": stock,
    "desc": desc,
    }
    addproductController(newProduct)
    return redirect('/products')


@app.route("/addproduct")
@login_required
def addproduct():
    # Redirect us to the product creation page
    return render_template("add_product.html")


@app.route("/accounts")
@login_required
def accounts():
    if request.method == 'GET' and 'userType' in request.args:
        userType = request.args.get('userType')
    else:
        # Otherwise default to customer
        userType = 'customer'

    # Retrieve all accounts from 'database' and redirect us to accounts page
    # -> accountsController.py
    acc = getaccounts(userType)
    return render_template("accounts.html", accounts=acc, userType=userType)


@app.route("/createaccount")
@login_required
def createaccount():
    userType = request.args.get('userType')
    # Redirect us to account creation page
    return render_template("create_account.html", userType=userType)


@app.route("/accountinfo", methods=['POST'])
@login_required
def accountinfo():
    userType = request.args.get('userType')
    print("Account info called")
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
    cname = request.form.get('card_name')
    cnumber = request.form.get('card_number')
    ctype = request.form.get('card_type')
    cdate = request.form.get('exp_date')
        # Process register info here
    
    isAdmin = True if userType == "administrator" else False

    if not isAdmin:
        newAccount = {
        "first_name": fname,
        "last_name": lname,
        "email": email,
        "password": pass1,
        "phone_number": pnumber,
        "status": "Active",
        "address_line_1": aline1,
        "address_line_2": aline2,
        "city": city,
        "state": state,
        "zipcode": zipcode,
        "card_name": cname,
        "card_type": ctype,
        "exp_date": cdate,
        "card_num": cnumber
        }
    else:
        newAccount = {
        "first_name": fname,
        "last_name": lname,
        "email": email,
        "password": pass1,
        "phone_number": pnumber,
        "status": "Active"
        } 
    
    addaccount(newAccount, isAdmin)
    return redirect("accounts?userType=" + userType)


@app.route("/editaccount", methods=['POST'])
@login_required
def editaccount():
    userType = request.args.get('userType')
    acc = request.args.get('acc')

    print(userType)
    # Fetch account given via url and then enter the edit page for that account
    isAdmin = True if userType == 'admin' else False
    account = getaccount(acc, isAdmin)
    return render_template("single_account.html", userType=userType, acc=account, account=acc)

@app.route("/updateaccount", methods=['POST'])
def updateaccount():
    id = request.form.get('id')
    userType = request.form.get('userType')
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    phone_number = request.form.get('pnumber')
    status = request.form.get('group1')

    if userType == 'customer':
        aline1 = request.form.get('aline1')
        aline2 = request.form.get('aline2')
        city = request.form.get('city')
        state = request.form.get('state')
        zipcode = request.form.get('zipcode')
        cname = request.form.get('cname')
        cnumber = request.form.get('cnumber')
        ctype = request.form.get('ctype')
        cdate = request.form.get('cdate')
        userInfo = [fname, lname, aline1, aline2, city, state, zipcode, phone_number, cname,
                    ctype, cnumber, cdate, status]
        updateAccountController(userInfo, userType, id)
    else:
        userInfo = [fname, lname, phone_number, status]
        # Our user info will depend on whether we're updating an admin or customer
        # -> accountsController.py
        updateAccountController(userInfo, userType, id)

    # Go back to edit page with message
    return redirect(url_for('editaccount', acc=id, userType=userType, message='added'))


@app.route("/editinfo", methods=['POST'])
@login_required
def editinfo():
    userType = request.args.get('userType')
    acc = request.args.get('acc')

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

    isAdmin = True if userType == 'admin' else False
    if not isAdmin:
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
    else:
        editAccount = {
        "a_first_name": fname,
        "a_last_name": lname,
        "a_email": email,
        "a_password": pass1,
        "a_phone_number": pnumber,
        "a_status": "Active"
        } 
    
    if userType != None and acc != None:
        editaccountcontroller(acc, editAccount, isAdmin)
        acc = getaccounts(isAdmin)
        return redirect('/accounts?userType=' + userType)
    else:
        editAccount = {
        "a_first_name": fname,
        "a_last_name": lname,
        "a_email": email,
        "a_password": pass1,
        "a_phone_number": pnumber,
        "a_status": "Active"
        } 
        editaccountcontroller(session['admin'], editAccount, True)
        return redirect('/profile')


@app.route("/orders")
@login_required
def orders():
    # Fetches all the orders found in the 'database' to bring to orders page
    all_orders = ordersController()  # ->connects to ordersModel
    return render_template("orders.html", orders=all_orders)


@app.route('/editorder')
@login_required
def editorder():
    order = request.args.get('order')
    # Receive from orders page an order via its id -> order
    # Fetch the products in that order
    orderProducts = getorderproducts(order)
    # Fetch the order itself. Overwrite order as the ID alone is no longer needed
    order = getorder(order)
    # Go to separate page for that order
    return render_template('order.html', products=orderProducts, order=order)

  
@app.route("/reports")
@login_required
def reports():
    return render_template("reports.html")


@app.route("/report", methods=['GET'])
@login_required
def report():
    # Initialize variables to use
    report = []
    report_cols = []
    total = 0

    # If we're going for any of the reports that have a date, get the information and save in date_report
    # All cases give the same results in this case, no matter your date or product input
    if request.args.get('report') == 'day':
        report, report_cols = getDatedReportDay(request.args.get('report_day'))
    elif request.args.get('report') == 'week':
        report = getDatedReportWeek(request.args.get('report_week'))
    elif request.args.get('report') == 'month':
        report = getDatedReportMonth(request.args.get('report_month'))
        
    # If we're going for the inventory/stock report, get the data and save in stock_report
    elif request.args.get('report') == 'inventory':
        report = getStockReport()

    # If we're going for any of the reports with dates, we need a total at the end
    # Calculate the total according to the sum of the total_prices for each item in the report
    # if report != {}:
    #     for keyorder in report:
    #         total += order['total_price']

    # We send to the report page all variables whether empty or not
    # The HTML will validate which variable is empty and will show the appropriate information
    
    print("Report:", report)
    report_type = request.args.get('report')

    return render_template("report.html", report=report, report_cols=report_cols, report_type=report_type)


# Press the green button in the gutter to run the script.
if __name__ == '__admin__':
    app.run(debug=True)
