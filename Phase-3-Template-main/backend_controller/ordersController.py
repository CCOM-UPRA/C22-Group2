from backend_model.ordersModel import *


def ordersController():
    return ordersModel()


def filterOrder(search, column):
    return filterOrdersModel(search, column)


def getorder(ID):
    return getordermodel(ID)


def getorderproducts(ID):
    return getorderproductsmodel(ID)
