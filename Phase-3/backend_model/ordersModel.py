# from backend_model.profileModel import MagerDicts
#
# # ORDER 1
# # ------------------------------------------------------------
# #
# orderDict1 = {"1": {
#     "tracking_num": "71287249",
#     "order_date": "01/17/23",
#     "arrival_date": "01/20/23",
#     "address_line_1": "Vista Azulin Calle 11 L13",
#     "address_line_2": "Arecibor Puerto Ricor, 00614",
#     "total": 144.97,
#     'total_items': 3,
#     "payment_method": "Mastercard",
#     'status': 'received'
# }}
#
# # ORDER 2
# # ------------------------------------------------------------
# #
# orderDict2 = {'2': {
#     "tracking_num": "92391290",
#     "order_date": "01/17/23",
#     "arrival_date": "01/20/23",
#     "address_line_1": "Vista Azulin Calle 11 L13",
#     "address_line_2": "Arecibor Puerto Ricor, 00614",
#     "total": 109.97,
#     'total_items': 3,
#     "payment_method": "Mastercard",
#     'status': 'delivered'
#
# }}
#
# # ORDER 3
# # ------------------------------------------------------------
# #
# orderDict3 = {'3': {
#     "tracking_num": "85277469",
#     "order_date": "01/17/23",
#     "arrival_date": "01/20/23",
#     "address_line_1": "Vista Azulin Calle 11 L13",
#     "address_line_2": "Arecibor Puerto Ricor, 00614",
#     "total": 49.98,
#     'total_items': 2,
#     "payment_method": "Mastercard",
#     'status': 'processed'
# }}
#
# # ORDER 4
# # ------------------------------------------------------------
# #
# orderDict4 = {'4': {
#     "tracking_num": "66788539",
#     "order_date": "01/17/23",
#     "arrival_date": "01/20/23",
#     "address_line_1": "Vista Azulin Calle 11 L13",
#     "address_line_2": "Arecibor Puerto Ricor, 00614",
#     "total": 24.99,
#     "total_items": 1,
#     "payment_method": "Mastercard",
#     'status': 'cancelled'
# }}
#
#
#
# # PRODUCTS
# # ------------------------------------------------------------
# productDict1 = {"1": {
#     "image": 'goldenballcactus.jpg',
#     "name": 'Golden Ball Cactus',
#     "family type": 'Cactus',
#     "price": 64.99,
#     "quantity": 1,
#     "total_price": 64.99,
#     "order_id": '1'
# }}
#
# productDict2 = {"2": {
#     "image": 'rose.jpg',
#     "name": 'Rose',
#     "family type": 'Flowers',
#     "price": 39.99,
#     "quantity": 2,
#     "total_price": 79.98,
#     "order_id": '1'
# }}
#
# productDict3 = {"3": {
#     "image": 'MonsteraDeliciosa.jpg',
#     "name": 'Monstera Deliciosa',
#     "family type": 'Araceae',
#     "price": 34.99,
#     "quantity": 2,
#     "total_price": 69.98,
#     "order_id": '2'
# }}
#
# productDict4 = {"4": {
#     "image": 'anthurium.jpg',
#     "name": 'Anthurium',
#     "family type": 'Araceae',
#     "price": 39.99,
#     "quantity": 1,
#     "total_price": 39.99,
#     "order_id": '2'
# }}
#
# productDict5 = {"5": {
#     "image": 'mooncactus.jpg',
#     "name": 'Moon Cactus',
#     "family type": 'Cactus',
#     "price": 24.99,
#     "quantity": 2,
#     "total_price": 49.98,
#     "order_id": '3'
# }}
#
# productDict6 = {"6": {
#     "image": 'sunflower.jpg',
#     "name": 'Sunflower',
#     "family type": 'Flowers',
#     "price": 24.99,
#     "quantity": 1,
#     "total_price": 24.99,
#     "order_id": '4'
# }}
#
#
# ordersList = MagerDicts(orderDict1, orderDict2)
# ordersList = MagerDicts(ordersList, orderDict3)
# ordersList = MagerDicts(ordersList, orderDict4)
#
# productsList = MagerDicts(productDict1, productDict2)
# productsList = MagerDicts(productsList, productDict3)
# productsList = MagerDicts(productsList, productDict4)
# productsList = MagerDicts(productsList, productDict5)
# productsList = MagerDicts(productsList, productDict6)
#

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




