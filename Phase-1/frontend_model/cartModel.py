from flask import session

# Dictionary uniter
def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False


# Cart items simulated
dictitems1 = {'1': {'name': "Tello Drone", 'price': 89.00, 'quantity': 2, 'total_price': 178.00,
                  'stock': 15, 'brand': "DJI", 'wifi': "Yes", 'videores': "480p", 'desc': "Tello Drone description",
                  'image': "dji_tello.jpg", 'cost': 89.00}}
dictitems2 = {'3': {'name': "F11 Pro", 'price': 399.00, 'quantity': 1, 'total_price': 399.00,
                  'stock': 10, 'brand': "Ruko", 'wifi': "Yes", 'videores': "4k", 'desc': "F11 Pro description",
                  'image': "ruko_f11_pro.jpg", 'cost': 350.00}}

def getCartModel():
    # Checking if cart is in session or not and adding the dictionaries to it
    if 'cart' in session:
        session['cart'] = MagerDicts(session['cart'], dictitems1)
    else:
        session['cart'] = dictitems1

    if 'cart' in session:
        session['cart'] = MagerDicts(session['cart'], dictitems2)
    else:
        session['cart'] = dictitems2

    return


def addCartModel():
    # make changes to cart here
    # not in use at the moment
    return


def deleteCartItemModel():
    # delete item from cart
    # not in use at the moment
    return



