from frontend_model.cartModel import *


def getCart():
    return getCartModel()


def addCartController(p_id, quantity):
    return addCartModel(p_id, quantity)


def deleteCartItem(p_id):
    return deleteCartItemModel(p_id)

