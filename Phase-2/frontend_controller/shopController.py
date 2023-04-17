from frontend_model.shopModel import *


def getProducts():
    return getProductsModel()

def searchProducts(search_query, filters = None):
    return searchProductsModel(search_query, filters)

def getSortingPreference():
    return getSortingPreferenceModel()

def getSortingByOrderPreference():
    return getSortingByOrderPreferenceModel()

def getLocation():
    return getLocationModel()

def getPlantType():
    return getPlantTypeModel()

def getSunExpo():
    return getSunExpoModel()


def getWatering():
    return getWateringModel()

def get_filtered_products(min_price=None, max_price=None, locations=None, plantType=None):
    return get_filtered_products_model(min_price, max_price, locations, plantType)

# def getFilteredProducts(sortings=None, orderBy=None, locations=None, plantType=None,sun=None,watering=None):
#     return getFilteredProductsModel(sortings, orderBy, locations, plantType,sun,watering)