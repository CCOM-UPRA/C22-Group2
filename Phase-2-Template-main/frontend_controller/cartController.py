from frontend_model.cartModel import *


def getCart():
    # Go to cartModel to get cart items and session variables: total and quantity
    return getCartModel()


def addCartController(p_id, name, image, price, quantity, total):
    # Receive the variables that we got from POST originally and save in a dictItem to add to session cart
    # The add happens over at the cartModel
    dictitems = {p_id: {'name': name, 'image': image, 'price': price, 'quantity': quantity,
                        'total_price': total}}
    return addCartModel(dictitems)


def deleteCartItem():
    # FOR STUDENT TO ADD
    return deleteCartItemModel()



