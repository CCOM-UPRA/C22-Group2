import json
# This is our simulation of the database
# We have two products here.
# The students must create their own productList when working on their eCommerce site
# Product images are loaded into static/images/product-images/
# Done in array instead of dictionaries to portray the differences

# Load JSON data into a dictionary
with open('JSONfiles/products.json') as f:
    data = json.load(f)

# Access keys and sub-keys and put them into a Python list
productList = []
for key in data.keys():
    item = [key]
    for sub_key in data[key].keys():
        item.append(data[key][sub_key])
    productList.append(item)

def getProductsModel():
    return productList


def getBrandsModel():
    # Simulating grabbing these filters via SQL from the database
    brands = ["Indoors", "Outdoors"]
    return brands

def getColorsModel():
    colors = ["White", "Gray", "Red"]
    return colors


def getVideoResModel():
    videores = ["480p", "1080p", "4k"]
    return videores


def getWifiModel():
    wifi = ['Yes', 'No']
    return wifi