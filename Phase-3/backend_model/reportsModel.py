import json

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


def getDatedReportModel():
    return ordersList


def getStockReportModel():
    
    return productsList
