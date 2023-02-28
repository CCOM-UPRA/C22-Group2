from flask import Flask, render_template, redirect, request, session, url_for
from backend_controller.loginController import *
from backend_controller.ordersController import ordersController, getorder, getorderproducts
from backend_controller.productsController import *
from backend_controller.accountsController import *
from backend_controller.reportsController import getDatedReport, getStockReport
from backend_controller.profileController import *

# In this template, you will usually find functions with comments tying them to a specific controller
# main.py accesses the frontend folders
# Every controller accesses its relevant model and will send the information back to this Flask app

app = Flask(__name__, template_folder='backend/')
app.secret_key = 'akeythatissecret'


@app.route("/", defaults={'message': None})
@app.route("/<message>")
def enterpage(message):
    return login()


@app.route("/clear")
def clear():
    # Clear session information
    session.clear()
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
def profile():
    admin = getUser(session['admin'])
    return render_template("profile.html", user1=admin)


@app.route("/password", methods=["POST"])
def password():
    # make password changes
    # optional for students to implement or not
    return render_template("change-password.html")


@app.route("/products")
def products():
    productsp = getProducts()
    return render_template("products.html", products=productsp)


@app.route("/product/<prod>")
def product(prod):
    return redirect(url_for('single_product', prodID=prod))


@app.route("/single_product/<prodID>")
def single_product(prodID):
    # Return product page for single product selected
    product = getsingleproduct(prodID)
    print("The product: ", product)
    return render_template("single_product.html", prod=product)


@app.route("/editproduct", methods=['POST'])
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
def addproduct():
    # Redirect us to the product creation page
    return render_template("add_product.html")

@app.route("/accounts/<userType>")
#@app.route("/accounts")
def accounts(userType = 'user'):
    # Retrieve all accounts from 'database' and redirect us to accounts page
    if userType == 'admin':
        isAdmin = True
    else:
        isAdmin = False
    acc = getaccounts(isAdmin)
    return render_template("accounts.html", accounts=acc, userType=userType)

@app.route("/createaccount/<userType>")
def createaccount(userType):
    # Redirect us to account creation page
    return render_template("create_account.html", userType=userType)


@app.route("/accountinfo/<userType>", methods=['POST'])
def accountinfo(userType):
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
    cname = request.form.get('cname')
    cnumber = request.form.get('cnumber')
    ctype = request.form.get('ctype')
    cdate = request.form.get('cdate')
        # Process register info here
        
    newAccount = {
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
    
    isAdmin = True if userType == "admin" else False
    addaccount(newAccount, isAdmin)
    return redirect('/accounts')


@app.route("/editaccount/<userType>/<acc>")
def editaccount(userType, acc):
    print(userType)
    # Fetch account given via url and then enter the edit page for that account
    isAdmin = True if userType == 'admin' else False
    account = getaccount(acc, isAdmin)
    return render_template("single_account.html", userType=userType, acc=account, account=acc)

@app.route("/editinfo", methods=['POST'])
@app.route("/editinfo/<userType>/<acc>", methods=['POST'])
def editinfo(userType = None, acc = None):
    
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
    
    if userType != None and acc != None:
        isAdmin = True if userType == 'admin' else False
        editaccountcontroller(acc, editAccount, isAdmin)
        return redirect('/accounts/' + userType)
    else:
        editaccountcontroller(session['admin'], editAccount, True)
        return redirect('/profile')

@app.route("/orders")
def orders():
    # Fetches all the orders found in the 'database' to bring to orders page
    all_orders = ordersController()  # ->connects to ordersModel
    return render_template("orders.html", orders=all_orders)


@app.route('/editorder/<order>')
def editorder(order):
    # Receive from orders page an order via its id -> order
    # Fetch the products in that order
    orderProducts = getorderproducts(order)
    # Fetch the order itself. Overwrite order as the ID alone is no longer needed
    order = getorder(order)
    # Go to separate page for that order
    return render_template('order.html', products=orderProducts, order=order)

  
@app.route("/reports")
def reports():
    return render_template("reports.html")


@app.route("/report", methods=['POST'])
def report():
    # Initialize variables to use
    date_report = {}
    stock_report = {}
    total = 0

    # If we're going for any of the reports that have a date, get the information and save in date_report
    # All cases give the same results in this case, no matter your date or product input
    if 'report_day' in request.form:
        date_report = getDatedReport()
    if 'report_week' in request.form:
        date_report = getDatedReport()
    if 'report_month' in request.form:
        date_report = getDatedReport()

    # If we're going for the inventory/stock report, get the data and save in stock_report
    if 'stock_report' in request.form:
        stock_report = getStockReport()

    # If we're going for any of the reports with dates, we need a total at the end
    # Calculate the total according to the sum of the total_prices for each item in the report
    if date_report != {}:
        for key, order in date_report.items():
            total += order['total_price']

    # We send to the report page all variables whether empty or not
    # The HTML will validate which variable is empty and will show the appropriate information
    return render_template("report.html", date_report=date_report, stock_report=stock_report, total=total)


# Press the green button in the gutter to run the script.
if __name__ == '__admin__':
    app.run(debug=True)
