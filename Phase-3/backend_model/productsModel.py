from classes.db_connect import DBConnect
from random import randrange
import json

productsPath = './JSONfiles/products.json'

# Merge dictionaries
def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False

# Done in array instead of dictionaries to portray the differences between dictionaries and arrays
# Database tuples are normally received in an array

def getProductsModel():
    db = DBConnect()
    query = "SELECT * FROM product"
    result = db.query(query)
    return result

# Find the specific product given the ID, found in element 0 of the sub-arrays
def getsingleproductmodel(prodID):
    db = DBConnect()
    query = "SELECT * FROM product WHERE product_id = %s"
    result = list(db.query(query,(prodID))).pop()
    return result

# Add a new product to the JSON file
def addproductmodel(name, plant_type, sun_exposure, watering, location, price, cost, stock, desc, image, status):
    db = DBConnect()
    sql = "INSERT INTO product (name, location, plant_type, sun_exp, watering, image, price, cost, stock, description, status) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    try:
        db.execute(sql,(name, location, plant_type, sun_exposure, watering, image, price, cost, stock, desc, status))

    except Exception as e:
        db.rollback()
        print(f"Error occurred: {e}")
        return None
    

def editproductmodel(product_id, name, plant_type, sun_exposure, watering, location, price, cost, stock, desc, image, status):
    db = DBConnect()
    sql = """UPDATE product SET name = %s, location = %s, plant_type = %s, sun_exp = %s, watering = %s, image = %s, price = %s,
      cost = %s, stock = %s, description = %s, status = %s WHERE product_id = %s"""
    try:
        db.execute(sql,(name, location, plant_type, sun_exposure, watering, image, price, cost, stock, desc, status, product_id))

    except Exception as e:
        db.rollback()
        print(f"Error occurred: {e}")
        return None