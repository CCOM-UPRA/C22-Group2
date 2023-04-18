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

#Searching a product by name
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



#-----------Implementing the filters

#def getFilteredProductsModel(sortings=None, orderBy=None, locations=None, plantType=None,sun=None,watering=None):
    db = DBConnect()

    # Start building the query and parameters
    query = "SELECT * FROM product WHERE 1=1"
    params = []

    # Apply the location filter
    if locations:
        query += " AND location IN ({})".format(','.join(['%s'] * len(locations)))
        params.extend(locations)

    # Apply the family type (plant type) filter
    if plantType:
        query += " AND plant_type IN ({})".format(','.join(['%s'] * len(plantType)))
        params.extend(plantType)

    # Execute the query with the built parameters
    result = db.query(query, params)
    return result
def get_filtered_products_model(sortings=None, sortByOrder=None, locations=None, plantType=None,sun=None,watering=None):
    db = DBConnect()

    # Start building the query and parameters
    query = "SELECT * FROM product WHERE 1=1"
    params = []

    # Apply the location filter
    if locations:
        query += " AND location IN ({})".format(','.join(['%s'] * len(locations)))
        params.extend(locations)

    # Apply the plant type filter
    if plantType:
        query += " AND plant_type IN ({})".format(','.join(['%s'] * len(plantType)))
        params.extend(plantType)


    #Apply the sun exposure filter
    if sun:
        query += " AND sun_exp IN ({})".format(','.join(['%s'] * len(sun)))
        params.extend(sun)

    #Apply the watering filter
    if watering:
        query += " AND watering IN ({})".format(','.join(['%s'] * len(watering)))
        params.extend(watering)

    #Apply the sorting by name or price filter
    if sortings:
        query += " AND ORDER BY ({})".format(','.join(['%s'] * len(sortings)))
        params.extend(sortings)

    #Apply the sorting by asc or desc
    if sortByOrder:
        query += "  ({})".format(','.join(['%s'] * len(sortByOrder)))
        params.extend(sortByOrder) 


    # Execute the query with the built parameters
    result = db.query(query, params)
    return result

 