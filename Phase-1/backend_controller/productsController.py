from backend_model.productsModel import *


def getProducts():
    products = getProductsModel()
    return products


def getsingleproduct(prodID):
    return getsingleproductmodel(prodID)