from backend_model.ordersModel import *


def ordersController():
    return ordersModel()


def getorder(ID):
    return getordermodel(ID)


def getorderproducts(ID):
    return getorderproductsmodel(ID)
