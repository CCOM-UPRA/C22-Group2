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



#-----------Define the filters

def getProductsByWateringModel(filter_query):
    db = DBConnect()
    to_filter = f"%{filter_query}%"
    query = "SELECT * FROM products WHERE watering = '%s'"
    result = db.query(query,(to_filter))
    return result













def getFilteredProductsModel(sortings=None, orderBy=None, locations=None, plantType=None,sun=None,watering=None):
    db = DBConnect()
    query = "SELECT * FROM product"
    filters = []
    if locations:
        filters.append(f"location='{locations}'")
    if plantType:
        filters.append(f"plant_type='{plantType}'")
    if sun:
        filters.append(f"sun_exp='{sun}'")
    if watering:
        filters.append(f"watering='{watering}'")
    if filters:
        query += " WHERE " + " AND ".join(filters)
    result = db.query(query)
    return result
    # db = DBConnect()
    # query = "SELECT * FROM product "
    # params = []
    
    # if locations:
    #     query += " AND location IN ({})".format(','.join(['%s'] * len(locations)))
    #     params.extend(locations)
    #    # query+=" WHERE location = %s"



    # # Apply the sortings filter
    # # if sortings:
    # #     query += " ORDER BY %s"
    # #     params.append(sortings)

    

    # # if max_price:
    # #     query += " AND price <= %s"
    # #     params.append(max_price)

    # # # Apply the location filter
    # # if locations:
    # #     query += " AND location IN ({})".format(','.join(['%s'] * len(locations)))
    # #     params.extend(locations)

    # # # Apply the family type (plant type) filter
    # # if family_types:
    # #     query += " AND plant_type IN ({})".format(','.join(['%s'] * len(family_types)))
    # #     params.extend(family_types)

    # # Execute the query with the built parameters
    # result = db.query(query, params)
    # return result
    