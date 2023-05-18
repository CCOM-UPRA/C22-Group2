from backend_model.productsModel import *


def getProducts(search_query):
    return getProductsModel(search_query)


def getsingleproduct(prodID):
    return getsingleproductmodel(prodID)

def addproductController(name, plant_type, sun_exposure, watering, location, price, cost, stock, desc, image, status):
    return addproductmodel(name, plant_type, sun_exposure, watering, location, price, cost, stock, desc, image, status)
    

def editproductController(product_id, name, plant_type, sun_exposure, watering, location, price, cost, stock, desc, image, status):
    editproductmodel(product_id, name, plant_type, sun_exposure, watering, location, price, cost, stock, desc, image, status)
    print("Product edited")

def updateImageFilename(product_id, new_filename):
    updateImageFilenamemodel(product_id, new_filename)

def getproductimage(product_id):
    return getproductimagemodel(product_id)