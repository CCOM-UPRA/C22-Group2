# Done in array instead of dictionaries to portray the differences between dictionaries and arrays
# Database tuples are normally received in an array
productList = [['1', "Tello Drone", 'DJI', 'desc here', 'Yes', '480p', 'White', 'dji_tello.jpg', '15', 'active', '89.00', '89.00'],
               ['2', 'Bebop 2', 'Parrot', 'desc', 'Yes', '1080p', 'Red', 'parrot_bebop_2.jpg', '3', 'active', '270.00', '290.00']]


def getProductsModel():
    return productList


# Find the specific product given the ID, found in element 0 of the sub-arrays
def getsingleproductmodel(prodID):
    for product in productList:
        if product[0] == prodID:
            return product
