from frontend_model.ordersModel import *


def getorder():
    return get_customer_order()

def getOrderIDs(customer_id):
    return getOrdersIDsModel(customer_id)