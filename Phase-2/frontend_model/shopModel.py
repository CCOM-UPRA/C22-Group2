from classes.db_connect import DBConnect
# This is our simulation of the database
# We have two products here.
# The students must create their own productList when working on their eCommerce site
# Product images are loaded into static/images/product-images/
# Done in array instead of dictionaries to portray the differences



def getProductsModel():
    productList = []
    db = DBConnect()
    Query = "SELECT * FROM product"
    result = db.query(Query)
    return result

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
