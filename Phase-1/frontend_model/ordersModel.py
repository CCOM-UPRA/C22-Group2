# Dictionary uniter
def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False


# Simulated database of orders and their products
# order1 contains productsOrder1...
order1 = {"tracking_num": "71287249",
    "order_date": "01/17/23",
    "arrival_date": "01/20/23",
    "address_line_1": "Vista Azulin Calle 11 L13",
    "address_line_2": "Arecibor Puerto Ricor, 00614",
    "total": 1197.00,
    "amount": 3,
    "payment_method": "Mastercard",
    "status": 'shipped'}

order2 = {"tracking_num": "92391290",
    "order_date": "01/20/23",
    "arrival_date": "01/23/23",
    "address_line_1": "Vista Azulin Calle 11 L13",
    "address_line_2": "Arecibor Puerto Ricor, 00614",
    "total": 629.00,
    "amount": 3,
    "payment_method": "Mastercard",
    "status": 'delivered'}

productDict1 = {"1": {
    "image": 'goldenballcactus.jpg',
    "name": 'Golden Ball Cactus',
    "family": 'Cactus',
    "price": 65.75,
    "quantity": 1,
    "total_price": 65.75
}}

productDict2 = {"2": {
    "image": 'rose.jpg',
    "name": 'Rose',
    "family": 'Flowers',
    "price": 59.99,
    "quantity": 2,
    "total_price": 119.98
}}

productsOrder1 = productDict1
productsOrder1 = MagerDicts(productsOrder1, productDict2)

productDict3 = {"3": {
    "image": 'MonsteraDeliciosa.jpg',
    "name": 'Monstera Deliciosa',
    "family": 'Araceae',
    "price": 35.00,
    "quantity": 2,
    "total_price": 70.00
}}

productDict4 = {"4": {
    "image": 'anthurium.jpg',
    "name": 'Anthurium',
    "family": 'Araceae',
    "price": 45.50,
    "quantity": 1,
    "total_price": 45.50
}}

productsOrder2 = productDict3
productsOrder2 = MagerDicts(productsOrder2, productDict4)


def getorder1M():
    return order1


def getorder2M():
    return order2


def getorder1prodM():
    return productsOrder1


def getorder2prodM():
    return productsOrder2




