import json

productsPath = './JSONfiles/products.json'
# This is our simulation of the database
# We have two products here.
# The students must create their own productList when working on their eCommerce site
# Product images are loaded into static/images/product-images/
# Done in array instead of dictionaries to portray the differences



def getProductsModel():
    
    # Load JSON data into a dictionary
    with open(productsPath) as f:
        data = json.load(f)

    # Access keys and sub-keys and put them into a Python list
    # productList = []
    # for key in data.keys():
    #  item = [key]
    # for sub_key in data[key].keys():
    #     item.append(data[key][sub_key])
    # productList.append(item)

    return dict(data)


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
