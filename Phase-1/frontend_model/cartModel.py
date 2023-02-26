from flask import session

# Dictionary uniter
def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False


# Cart items simulated
dictitems1 = {'1': {'name': "Echeveria", 'price': 13.75, 'quantity': 2, 'total_price': 27.50,
                  'stock': 15, 'family type': "Succulents", 'water': "Weekly", 'sun': "Part Sun", 'desc': "Echeverias description",
                  'image': "echeverias.jpg", 'location': "Indoors"}}
dictitems2 = {'2': {'name': "Kalanchoe", 'price': 20.50, 'quantity': 1, 'total_price': 20.50,
                  'stock': 10, 'family type': "Succulents", 'water': "Biweekly", 'sun': "Full Sun", 'desc': "Kalanchoe description",
                  'image': "kalanchoe.jpg", 'location': "Outdoor"}}


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



