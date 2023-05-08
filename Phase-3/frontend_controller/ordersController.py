from frontend_model.ordersModel import *


def getorder():
    return get_customer_order()

def get_orders_and_products(customer_id):
    return get_orders_and_products_model(customer_id)

def getOrderIDs(customer_id):
    return getOrdersIDsModel(customer_id)