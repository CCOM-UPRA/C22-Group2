import json
from classes.db_connect import DBConnect
from datetime import datetime, timedelta
import calendar

# Open reports with dates 
with open("JSONfiles/inventory_report_dates.json") as f:
    ordersList = json.load(f)


# Open reports without dates 
with open("JSONfiles/inventory_report.json") as f:
    productsList = json.load(f)

# ordersList = dictProd1
# ordersList = MagerDicts(ordersList, dictProd2)
# ordersList = MagerDicts(ordersList, dictProd3)
# ordersList = MagerDicts(ordersList, dictProd4)
# ordersList = MagerDicts(ordersList, dictProd5)


# productsList = product1
# productsList = MagerDicts(productsList, product2)
# productsList = MagerDicts(productsList, product3)
# productsList = MagerDicts(productsList, product4)
# productsList = MagerDicts(productsList, product5)
# productsList = MagerDicts(productsList, product6)


def getDatedReportModel(report_type, date, product_id = None):
    db = DBConnect()
    
    if date == "" or date == None:
        date = datetime.today().date()
    
    if product_id:
        product_sql = " AND contains.product_id = %s "
    else:
        product_sql = ""
    
    if report_type == "day":
        sql = """SELECT name, order_date AS date, COALESCE(SUM(product_quantity), 0) AS sales, COALESCE(SUM(product_quantity * product_price), 0) AS total_price
            FROM orders RIGHT JOIN contains
            ON orders.order_id = contains.order_id
            LEFT JOIN product ON contains.product_id = product.product_id
            WHERE order_date = %s""" + product_sql + \
            """GROUP BY DAY(order_date), contains.product_id 
            ORDER BY name, DAY(order_date)"""
            
        if product_id:
            result = list(db.query(sql, (date, product_id)))
        else:
            result = list(db.query(sql, (date)))
        
    elif report_type == "week":
        sql = """SELECT name, order_date AS date, COALESCE(SUM(product_quantity), 0) AS sales, COALESCE(SUM(product_quantity * product_price), 0) AS total_price
            FROM orders RIGHT JOIN contains
            ON orders.order_id = contains.order_id
            LEFT JOIN product ON contains.product_id = product.product_id
            WHERE order_date BETWEEN %s AND %s""" + product_sql + \
            """GROUP BY DAY(order_date), contains.product_id 
            ORDER BY name, DAY(order_date)"""
        
        # Calculate the date of the previous Sunday
        date_object = datetime.strptime(str(date), '%Y-%m-%d')
        sunday = date_object - timedelta(days=date_object.weekday())

        # Calculate the date of the next Sunday
        saturday = sunday + timedelta(days=6)
        
        # Extract the first and last day of the week range
        first_day = sunday.date()
        last_day = saturday.date()
        
        if product_id:
            result = list(db.query(sql, (first_day, last_day, product_id)))
        else:
            result = list(db.query(sql, (first_day, last_day)))
            
    elif report_type == "month":
        sql = """SELECT name, order_date AS date, COALESCE(SUM(product_quantity), 0) AS sales, COALESCE(SUM(product_quantity * product_price), 0) AS total_price
            FROM orders RIGHT JOIN contains
            ON orders.order_id = contains.order_id
            LEFT JOIN product ON contains.product_id = product.product_id
            WHERE MONTH(order_date) = MONTH(%s) AND YEAR(order_date) = YEAR(%s)""" + product_sql + \
            """GROUP BY DAY(order_date), contains.product_id 
            ORDER BY name, MONTH(order_date), DAY(order_date)"""
            
        if product_id:
            result = list(db.query(sql, (str(date), str(date), product_id)))
        else:
            result = list(db.query(sql, (str(date), str(date))))
    else:
        return
    
    
     # Format total_price and date
    for row in result:
        row['total_price'] = '$' + format(row['total_price'], '.2f')
        date = row['date']
        
        day = date.day
        month = calendar.month_abbr[date.month]
        year = str(date.year)
        
        print(month, type(month))
        print(year, type(year))
        row['date'] = year + "-" + month + "-" + str(day)


    columns = [ "name", "date", "sales", "total_price"]
    
    print("The query: ", sql)
    print(result, columns)
    return result, columns

def getStockReportModel():
    db = DBConnect()
    sql = "SELECT product_id, name, stock, cost, price FROM product"
    result = db.query(sql)
    
    for row in result:
        row['cost'] = '$' + format(row['cost'], '.2f')
        row['price'] = '$' + format(row['price'], '.2f')
    
    columns = ["product_id", "name", "stock", "cost", "price"]
    return result, columns

def getProductsIDModel():
    db = DBConnect()
    sql = "SELECT product_id, name FROM product"
    return db.query(sql)

def getTodayDateModel():
    return str(datetime.today().date())