from frontend_model.invoiceModel import *

def getOrderProducts(id):
    return getOrderProductsModel(id)

def getOrder(id):
    return getOrderModel(id)

def addOrder(shipping_address, payment_method):
    return addOrderModel(shipping_address, payment_method)

# def getOrderProducts():
#     return getProductsModel()
