from frontend_model.shopModel import *


def getProducts():
    products = getProductsModel()
    return products


def getLocation():
    return getLocationModel()


def getFamilyType():
    return getFamilyModel()


def getSunExpo():
    return getSunExpoModel()


def getWatering():
    return getWateringModel()