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

def get_filtered_products(sortings=None, sortByOrder=None, locations=None, plantType=None,sun=None,watering=None, search_query=None):
    return get_filtered_products_model(sortings, sortByOrder, locations, plantType, sun,watering, search_query)

