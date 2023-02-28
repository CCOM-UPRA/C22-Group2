import json
from random import randrange
# from pathlib import Path
# Hacky fix
# path = Path(__file__).parent.parent.absolute()
productsPath = './JSONfiles/products.json'

def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False

# Done in array instead of dictionaries to portray the differences between dictionaries and arrays
# Database tuples are normally received in an array

def getProductsModel():
  # Load JSON data into a dictionary
  with open(productsPath) as f:
    data = json.load(f)
    return data

# Find the specific product given the ID, found in element 0 of the sub-arrays
def getsingleproductmodel(prodID):
    productList=[]

    for product in productList:
        if product[0] == prodID:
            return product

# Add a new product to the JSON file
def addproductmodel(prod : dict):
    path = productsPath
    currentFile = getProductsModel()
    # assign new key to product
    newKey = randrange(0, 999999999)
    while (newKey in currentFile.keys()):
        newKey = randrange(0, 999999999)

    newEntry = {str(newKey): dict(prod)}
    # add account to dictionary
    currentFile = MagerDicts(currentFile, newEntry)
    # write to json
    with open(path, "w") as f:
        json.dump(currentFile, f)