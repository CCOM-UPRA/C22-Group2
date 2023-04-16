from classes.db_connect import DBConnect
# This is our simulation of the database
# We have two products here.
# The students must create their own productList when working on their eCommerce site
# Product images are loaded into static/images/product-images/
# Done in array instead of dictionaries to portray the differences

#Products in database

def getProductsModel():
    db = DBConnect()
    query = "SELECT * FROM product"
    result = db.query(query)
    return result

#Searching a prudct by name
def searchProductsModel(search_query, filters = None):
    db = DBConnect()
    to_search = f"%{search_query}%"
    query = "SELECT * FROM product WHERE name LIKE %s"
    result = db.query(query, (to_search))
    return result


#-----------Define the models for the checkbox in /shop---------------

#These stays the same because they are not retrived from database
def getSortingPreferenceModel():
    sortings=["Name","Price"]
    return sortings

def getSortingByOrderPreferenceModel():
    orderBy=["Ascending","Descending"]
    return orderBy

#These are retrieved from the dataBase (all the disticts values for each categories)

def getLocationModel():
    db = DBConnect()
    query = "SELECT DISTINCT location FROM product"
    result = db.query(query)
    return result

def getPlantTypeModel():
    db = DBConnect()
    query = "SELECT DISTINCT plant_type FROM product"
    result = db.query(query)
    return result


def getSunExpoModel():
    db = DBConnect()
    query = "SELECT DISTINCT sun_exp FROM product"
    result = db.query(query)
    return result


def getWateringModel():
    db = DBConnect()
    query = "SELECT DISTINCT watering FROM product"
    result = db.query(query)
    return result