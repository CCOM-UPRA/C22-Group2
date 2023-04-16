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

def getFamilyType():
    return getPlantTypeModel()


def getSunExpo():
    return getSunExpoModel()


def getWatering():
    return getWateringModel()