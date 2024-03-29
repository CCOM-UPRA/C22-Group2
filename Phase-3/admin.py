import os
import uuid
from functools import wraps #TODO check
from datetime import datetime, timedelta
from time import strftime

from flask import Flask, render_template, redirect, request, session, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename

from backend_controller.loginController import *
from backend_controller.ordersController import ordersController, getorder, getorderproducts, edit_order
from backend_controller.productsController import *
from backend_controller.accountsController import *
from backend_controller.reportsController import *
from backend_controller.profileController import *

# Every controller accesses its relevant model and will send the information back to this Flask app

UPLOAD_FOLDER = 'static/images/product-images'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__, template_folder='backend/')
app.secret_key = 'akeythatissecret'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


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
        
        if message:
            return render_template('404.html')
        return redirect("/products")
    
    return redirect("/login")
    

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


@app.route("/products", methods=['GET'])
@login_required
def products():
    
    search_query = request.args.get("search_query")
    products = getProducts(search_query)
    return render_template("products.html", products=products, search_query=search_query)


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
    if len(product) == 0:
        return render_template('404.html')
    
    return render_template("single_product.html", prod=product)


@app.route("/editproduct", methods=['POST'])
@login_required
def editproduct():
    product_id = request.form.get('prod_id')
    # process the changes to a product's information
    print(request.files)
    print("Edit product called")
    if 'image' not in request.files:
        filename = getproductimage(product_id)['image']
    file = request.files['image']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        filename = getproductimage(product_id)['image']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # split filename into name and extension
        name_only, ext = os.path.splitext(filename)
        # use product_id for the new filename
        filename = "{}_{}{}".format(name_only, product_id, ext)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        # delete old file if it exists
        if os.path.isfile(file_path):
            os.remove(file_path)
        file.save(file_path)

    
    name = request.form.get('name')
    plant_type = request.form.get('plant_type')
    sun_exposure = request.form.get('sun_exposure')
    watering = request.form.get('watering')
    location = request.form.get('location')
    price = request.form.get('price')
    cost = request.form.get('cost')
    stock = request.form.get('stock')
    desc = request.form.get('desc')
    image = filename
    status = request.form.get('status')

    editproductController(product_id, name, plant_type, sun_exposure, watering, location, price, cost, stock, desc, image, status)
    return redirect('/products')


@app.route("/addproduct")
@login_required
def addproduct():
    # Redirect us to the product creation page
    return render_template("add_product.html")


@app.route("/add", methods=["POST"])
@login_required
def add():
    # check if the post request has the file part
    print(request.files)
    if 'image' not in request.files:
        flash('No file part')
    file = request.files['image']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('No selected file')
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # split filename into name and extension
        name_only, ext = os.path.splitext(filename)
        # use UUID for the temporary filename
        temp_filename = "{}{}".format(uuid.uuid4(), ext)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], temp_filename))
            
    name = request.form.get('name')
    plant_type = request.form.get('plant_type')
    sun_exposure = request.form.get('sun_exposure')
    watering = request.form.get('watering')
    location = request.form.get('location')
    price = request.form.get('price')
    cost = request.form.get('cost')
    stock = request.form.get('stock')
    desc = request.form.get('desc')
    image = temp_filename
    status = request.form.get('status')

    # get product_id from addproductController
    product_id = addproductController(name, plant_type, sun_exposure, watering, location, price, cost, stock, desc, image, status)
    
    if product_id is not None:
        # generate new filename with product_id and original filename
        new_filename = "{}_{}{}".format(name_only, product_id, ext)
        old_path = os.path.join(app.config['UPLOAD_FOLDER'], temp_filename)
        new_path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
        os.rename(old_path, new_path)
        
        # Update the image in the database with the new filename
        updateImageFilename(product_id, new_filename)
    else:
        print("Error: Product was not added to the database.")
        return redirect("/products")
        
    return redirect("/products")


@app.route("/accounts")
@login_required
def accounts():
    if request.method == 'GET' and 'userType' in request.args:
        userType = request.args.get('userType')
        if userType != 'customer' and userType != 'administrator':
            return render_template('404.html')
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
    
    if userType != 'customer' and userType != 'administrator':
        return render_template('404.html')
    
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
    status = request.form.get('status')
    
    # Process register info here

    if userType == 'customer' or userType == 'administrator':
        newAccount = [
            fname,
            lname,
            email,
            pass1,
            pnumber,
            status
        ]
    else:
        return render_template('404.html')
    
    addaccount(newAccount, userType)
    return redirect("accounts?userType=" + userType)


@app.route("/editaccount/<acc>", methods=['GET'])
@login_required
def editaccount(acc):
    # Fetch account given via url and then enter the edit page for that account
    # acc = customer or admin ID

    message = ""

    # Find userType, relevant for the query info
    if 'userType' in request.args:
        userType = request.args.get('userType')
    else:
        userType = 'customer'

    # Check if updateaccount() sent us a message of form completion to display
    if 'message' in request.args:
        message = request.args.get('message')

    # -> accountsController.py
    account = getaccount(acc, userType)
    
    if len(account) == 0:
        return render_template('404.html')
    print("Account ID: ", acc)
    print("UserType: ", userType)
    return render_template("single_account.html", acc=account, account=acc, userType=userType, message=message)


@app.route("/editinfo", methods=['POST'])
@login_required
def editinfo():
    acc = request.form.get('acc')
    userType = request.form.get('userType')
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    phone_number = request.form.get('pnumber')
    email = request.form.get('email')
    password = request.form.get('pass1')
    status = request.form.get('group1')

    if userType == 'customer':
        userInfo = [fname, lname, phone_number, email, password, status, acc]
        updateAccountcontroller(userInfo, userType)
    else:
        userInfo = [fname, lname, phone_number, email, password, status, acc]
        # Our user info will depend on whether we're updating an admin or customer
        # -> accountsController.py
        updateAccountcontroller(userInfo, userType)

    # Go back to edit page with message
    return redirect(url_for('editaccount', acc=acc, userType=userType, message='updated'))


@app.route("/editprofile", methods=["POST"])
def editprofile():
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

    return redirect("/profile")


@app.route("/orders")
@login_required
def orders():
    # Fetches all the orders found in the 'database' to bring to orders page
    all_orders = ordersController()  # ->connects to ordersModel
    return render_template("orders.html", orders=all_orders)


@app.route('/order', methods = ['GET'])
@login_required 
def order():
    order = request.args.get('order')    
    # Fetch the products in that order
    orderProducts = getorderproducts(order)
    # Fetch the order itself. Overwrite order as the ID alone is no longer needed
    order = getorder(order)
    
    if len(order) == 0:
        return render_template('404.html')
    else:
        return render_template('order.html', products=orderProducts, order=order)


@app.route('/editorder', methods=['POST'])
@login_required
def editorder():

    order = request.form.get('order')
    status = request.form.get('status')
    # Receive from orders page an order via its id -> order
    # Fetch the products in that order
    #orderProducts = getorderproducts(order)
    # Fetch the order itself. Overwrite order as the ID alone is no longer needed
    edit_order(status, order)
    #order = getorder(order)
    # Go to separate page for that order
    return redirect(request.referrer)

  
@app.route("/reports")
@login_required
def reports():
    products = get_products_id()
    return render_template("reports.html", products=products)


@app.route("/report", methods=['GET'])
@login_required
def report():
    # Initialize variables to use
    report = []
    report_cols = []
    total = 0

    report_type = request.args.get('report')
    report_date = request.args.get('report_date')
    product_id = request.args.get('product')
    
    if report_date == None or report_date == "":
        report_day = getTodayDate()
    else:
        report_day = report_date
        
    
    if request.args.get('report') == 'inventory':
        report, report_cols = getStockReport()
        
        if len(report) == 0:
            return render_template('404.html')
        
        return render_template("report.html", report=report, report_cols=report_cols, report_type=report_type, report_date=None, product_id=None)
    else:
        report, report_cols = getDatedReport(report_type, report_date, product_id)
        
        if len(report) == 0:
            return render_template('404.html')
        
        for i in report:
            total += float(i['total_price'].split("$")[1])
        
        total = f'{total:.2f}'
        
        return render_template("report.html", report=report, report_cols=report_cols, report_type=report_type, report_date=report_day, product_id=product_id, total=total)


# Press the green button in the gutter to run the script.
if __name__ == '__admin__':
    app.run(debug=True)
