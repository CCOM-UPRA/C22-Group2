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

#def getFilteredProducts(sortings, orderBy, locations, plantType,sun,watering):
# def getFilteredProducts(request):
#     locations = request.GET.get('location')
#     plantType = request.GET.get('plant_type')
#     sun = request.GET.get('sun_exp')
#     watering = request.GET.get('watering')
#     return getFilteredProductsModel(locations, plantType,sun,watering)
   # return getFilteredProductsModel(sortings, orderBy, locations, plantType,sun,watering)


def getProductsByWatering(filter_query):
    return getProductsByWateringModel(filter_query)