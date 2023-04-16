from classes.db_connect import DBConnect
# This is our simulation of the database
# We have two products here.
# The students must create their own productList when working on their eCommerce site
# Product images are loaded into static/images/product-images/
# Done in array instead of dictionaries to portray the differences



def getProductsModel():
    db = DBConnect()
    query = "SELECT * FROM product"
    result = db.query(query)
    return result

def searchProductsModel(search_query, filters = None):
    db = DBConnect()
    to_search = f"%{search_query}%"
    query = "SELECT * FROM product WHERE name LIKE %s"
    result = db.query(query, (to_search))
    return result

def getSortingPreferenceModel():
    sortings=["Name","Price"]
    return sortings

def getSortingByOrderPreferenceModel():
    orderBy=["Ascending","Descending"]
    return orderBy

def getLocationModel():
    # Simulating grabbing these filters via SQL from the database
    locations = ["Indoors", "Outdoors"]
    return locations

def getFamilyModel():
    family = ["Succulents", "Araceae", "Cactus", "Flowers"]
    return family


def getSunExpoModel():
    sun = ["Part Sun", "Full Sun", "Part Shade", "Full Shade"]
    return sun


def getWateringModel():
    watering = ['Weekly', 'Biweekly']
    return watering
