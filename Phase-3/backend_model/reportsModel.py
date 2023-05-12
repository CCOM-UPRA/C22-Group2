import json
from classes.db_connect import DBConnect
from datetime import datetime
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


def getDatedReportWeekModel():
    db = DBConnect()
    sql = """SELECT name, order_date AS date, COALESCE(SUM(product_quantity), 0) AS sales, COALESCE(SUM(product_quantity * product_price), 0) AS total_price
        FROM product 
        NATURAL JOIN contains
        NATURAL JOIN orders
        GROUP BY product_id, WEEK(order_date) 
        ORDER BY WEEK(order_date), DAY(order_date)"""
    
    result = list(db.query(sql))
    
        # Format total_price
    for row in result:
        row['total_price'] = '$' + format(row['total_price'], '.2f')
        date = row['date']
        
        day = date.day
        month = calendar.month_abbr[date.month]
        year = str(date.year)
        
        print(month, type(month))
        print(year, type(year))
        row['date'] = year + "-" + month + "-" + str(day)


    return result


def getStockReportModel():
    db = DBConnect()
    sql = "SELECT product_id, name, stock, cost, price FROM product"
    result = db.query(sql)
    
    for row in result:
        row['cost'] = '$' + format(row['cost'], '.2f')
        row['price'] = '$' + format(row['price'], '.2f')
    
    return result
