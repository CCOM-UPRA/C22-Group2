import json


orderDict = {
    "tracking_num": "71287249",
    "order_date": "01/17/23",
    "arrival_date": "01/20/23",
    "address_line_1": "Vista Azul Calle 11 L13",
    "address_line_2": "Arecibo Puerto Rico, 00614",
    "total": 0,
    "payment_method": "Mastercard"
    }


with open("JSONfiles/invoice_model.json","r") as file:
    products = json.load(file)

# getting order total
for key in products.keys():
    orderDict["total"] += products[key]["total_price"]


def getOrderModel():
    return orderDict


def getProductsModel():
    return products
