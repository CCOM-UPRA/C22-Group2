import json
# from pathlib import Path
# Hacky fix
# path = Path(__file__).parent.parent.absolute()
productsPath = './JSONfiles/products.json'

# Done in array instead of dictionaries to portray the differences between dictionaries and arrays
# Database tuples are normally received in an array

def getProductsModel():
  # Load JSON data into a dictionary
  with open(productsPath) as f:
    data = json.load(f)
    return data

# Find the specific product given the ID, found in element 0 of the sub-arrays
def getsingleproductmodel(prodID):
    productList = getProductsModel()
    return dict(productList).get(prodID)