from backend_model.connectDB import *

# Orders simulation for the reports that specify date
dictProd1 = {1: {'name': 'Tello Drone', 'brand': 'DJI', 'date': '2023-01-01', 'price': '89.00',
                 'quantity': 2, 'total_price': 178.00}}
dictProd2 = {2: {'name': 'F11 Pro', 'brand': 'Ruko', 'date': '2023-01-04', 'price': '399.00',
                 'quantity': 1, 'total_price': 399.00}}
dictProd3 = {3: {'name': 'F11 Pro', 'brand': 'Ruko', 'date': '2023-12-5', 'price': '399.00',
                 'quantity': 3, 'total_price': 1197.00}}
dictProd4 = {4: {'name': 'Bebop 2', 'brand': 'Parrot', 'date': '2023-04-12', 'price': '270.00',
                 'quantity': 1, 'total_price': 270.00}}
dictProd5 = {5: {'name': 'Premium X Star', 'brand': 'Autel Robotics', 'date': '2023-01-01', 'price': '1,399.00',
                 'quantity': 2, 'total_price': 2798.00}}


# Orders simulation for the inventory/stock report
product1 = {1: {'name': "Tello Drone", 'brand': 'DJI', 'quantity': 15}}
product2 = {2: {'name': "F11 Pro", 'brand': 'Ruko', 'quantity': 4}}
product3 = {3: {'name': "Bebop 2", 'brand': 'Parrot', 'quantity': 13}}
product4 = {4: {'name': "Premium X Star", 'brand': 'Autel Robotics', 'quantity': 25}}
product5 = {5: {'name': "Evo Quadcopter II", 'brand': 'Autel Robotics', 'quantity': 2}}
product6 = {6: {'name': "Mini 3 Pro", 'brand': 'DJI', 'quantity': 65}}


def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False


ordersList = dictProd1
ordersList = MagerDicts(ordersList, dictProd2)
ordersList = MagerDicts(ordersList, dictProd3)
ordersList = MagerDicts(ordersList, dictProd4)
ordersList = MagerDicts(ordersList, dictProd5)


productsList = product1
productsList = MagerDicts(productsList, product2)
productsList = MagerDicts(productsList, product3)
productsList = MagerDicts(productsList, product4)
productsList = MagerDicts(productsList, product5)
productsList = MagerDicts(productsList, product6)


def getReportModel(timeframe, query, start_date, end_date, product):
    db = Dbconnect()
    if timeframe == "Day":
        ordersFound = db.select(query, (start_date, product))

        for p in ordersFound:
            p['earnings'] = (float(p['p_price']) - float(p['p_cost'])) * int(p['product_quantity'])
        return ordersFound

    else:
        ordersFound = db.select(query, (start_date, end_date, product))
        for p in ordersFound:
            p['earnings'] = (float(p['p_price']) - float(p['p_cost'])) * int(p['product_quantity'])
            print(p)
        return ordersFound


def getNamesModel():
    # DB credentials found in backend_model/connectDB.py
    db = Dbconnect()
    query = "SELECT DISTINCT p_name FROM products ORDER BY p_name ASC"
    names = db.select(query)
    return names


def getDatedReportModel():
    return ordersList


def getStockReportModel():
    return productsList
