from backend_model.productsModel import *


def getProducts():
    return getProductsModel()


def getsingleproduct(prodID):
    return getsingleproductmodel(prodID)

def addproductController(prod : dict):
    print("Product added")
    addproductmodel(prod)