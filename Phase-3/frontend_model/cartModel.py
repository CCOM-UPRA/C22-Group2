from classes.db_connect import DBConnect
from flask import session

# Dictionary uniter
def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False


def getCartModel():
    # Checking if cart is in session or not and adding the dictionaries to it
    if 'cart' in session:
        return session['cart']
    else:
        session['cart'] = []
        return session['cart']


def deleteCartItemModel(p_id):
    # delete item from cart
    if 'cart' in session:
        for i in range(len(session['cart'])):
            if int(session['cart'][i]['product_id']) == int(p_id):
                new_list = session['cart']
                new_list.pop(i)
                session['cart'] = new_list
                break


def addCartModel(p_id, quantity):
    # make changes to cart here
    # not in use at the moment
    db = DBConnect()
    query = "SELECT * FROM `product` WHERE product_id = %s"
    result = list(db.query(query, (p_id))).pop()
    result = MagerDicts(result, {"quantity" : int(quantity), "total_price" : int(quantity) * round(result['price'],2)})

    if 'cart' in session:
        found = False
        for product in session['cart']:
            if int(product['product_id']) == int(p_id):
                product['quantity'] += result['quantity']
                product['total_price'] = round(result['total_price'], 2)
                found = True
                break
        if found == False:
            session['cart'] += [result]
    else:
        session['cart'] = [result]



