from backend_model.productsModel import *


def getProducts():
    return getProductsModel()


def getsingleproduct(prodID):
    return getsingleproductmodel(prodID)

def addproductController(name, plant_type, sun_exposure, watering, location, price, cost, stock, desc, image, status):
    addproductmodel(name, plant_type, sun_exposure, watering, location, price, cost, stock, desc, image, status)
    print("Product added")

def editproductController(product_id, name, plant_type, sun_exposure, watering, location, price, cost, stock, desc, image, status):
    editproductmodel(product_id, name, plant_type, sun_exposure, watering, location, price, cost, stock, desc, image, status)
    print("Product edited")