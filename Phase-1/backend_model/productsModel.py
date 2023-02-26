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

    # Access keys and sub-keys and put them into a Python list
    productList = []
    for key in data.keys():
     item = [key]
    for sub_key in data[key].keys():
        item.append(data[key][sub_key])
    productList.append(item)


    return productList


# Find the specific product given the ID, found in element 0 of the sub-arrays
def getsingleproductmodel(prodID):
    productList=[]

    for product in productList:
        if product[0] == prodID:
            return product
