from backend_model.profileModel import MagerDicts

# ORDER 1
# ------------------------------------------------------------
#
orderDict1 = {"1": {
    "tracking_num": "71287249",
    "order_date": "01/17/23",
    "arrival_date": "01/20/23",
    "address_line_1": "Vista Azulin Calle 11 L13",
    "address_line_2": "Arecibor Puerto Ricor, 00614",
    "total": 1197.00,
    "payment_method": "Mastercard",
    'status': 'delivered'
}}

# ORDER 2
# ------------------------------------------------------------
#
orderDict2 = {'2': {
    "tracking_num": "71287249",
    "order_date": "01/17/23",
    "arrival_date": "01/20/23",
    "address_line_1": "Vista Azulin Calle 11 L13",
    "address_line_2": "Arecibor Puerto Ricor, 00614",
    "total": 1197.00,
    "payment_method": "Mastercard",
    'status': 'shipped'

}}

# ORDER 3
# ------------------------------------------------------------
#
orderDict3 = {'3': {
    "tracking_num": "71287249",
    "order_date": "01/17/23",
    "arrival_date": "01/20/23",
    "address_line_1": "Vista Azulin Calle 11 L13",
    "address_line_2": "Arecibor Puerto Ricor, 00614",
    "total": 1197.00,
    "payment_method": "Mastercard",
    'status': 'processed'
}}

# ORDER 4
# ------------------------------------------------------------
#
orderDict4 = {'4': {
    "tracking_num": "71287249",
    "order_date": "01/17/23",
    "arrival_date": "01/20/23",
    "address_line_1": "Vista Azulin Calle 11 L13",
    "address_line_2": "Arecibor Puerto Ricor, 00614",
    "total": 1197.00,
    "payment_method": "Mastercard",
    'status': 'cancelled'
}}



# PRODUCTS
# ------------------------------------------------------------
productDict1 = {"1": {
    "image": 'ruko_f11_pro.jpg',
    "name": 'F11 Pro',
    "brand": 'Ruko',
    "price": 399.00,
    "quantity": 1,
    "total_price": 399.00,
    "order_id": '1'
}}

productDict2 = {"2": {
    "image": 'dji_tello.jpg',
    "name": 'Tello Drone',
    "brand": 'DJI',
    "price": 89.00,
    "quantity": 2,
    "total_price": 178.00,
    "order_id": '1'
}}

productDict3 = {"3": {
    "image": 'dji_tello.jpg',
    "name": 'Tello Drone',
    "brand": 'DJI',
    "price": 89.00,
    "quantity": 2,
    "total_price": 178.00,
    "order_id": '3'
}}

productDict4 = {"4": {
    "image": 'dji_tello.jpg',
    "name": 'Tello Drone',
    "brand": 'DJI',
    "price": 89.00,
    "quantity": 2,
    "total_price": 178.00,
    "order_id": '2'
}}

productDict5 = {"5": {
    "image": 'ruko_f11_pro.jpg',
    "name": 'F11 Pro',
    "brand": 'Ruko',
    "price": 399.00,
    "quantity": 1,
    "total_price": 399.00,
    "order_id": '4'
}}

productDict6 = {"6": {
    "image": 'ruko_f11_pro.jpg',
    "name": 'F11 Pro',
    "brand": 'Ruko',
    "price": 399.00,
    "quantity": 1,
    "total_price": 399.00,
    "order_id": '2'
}}


ordersList = MagerDicts(orderDict1, orderDict2)
ordersList = MagerDicts(ordersList, orderDict3)
ordersList = MagerDicts(ordersList, orderDict4)

productsList = MagerDicts(productDict1, productDict2)
productsList = MagerDicts(productsList, productDict3)
productsList = MagerDicts(productsList, productDict4)
productsList = MagerDicts(productsList, productDict5)
productsList = MagerDicts(productsList, productDict6)


def ordersModel():
    return ordersList


def getordermodel(ID):
    for key, order in ordersList.items():
        if key == ID:
            return order


def getorderproductsmodel(ID):
    returnList = {}
    num = 1
    for key, product in productsList.items():
        if product['order_id'] == ID:
            if returnList == {}:
                returnList = {'1': product}
            else:
                num += 1
                returnList = MagerDicts(returnList, {str(num): product})
    print(returnList)
    return returnList




