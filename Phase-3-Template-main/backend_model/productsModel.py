from backend_model.connectDB import *


def getProductsModel():
    # DB credentials found in backend_model/connectDB.py
    db = Dbconnect()
    productList = []

    query = "SELECT * FROM products"
    productsFound = db.select(query)

    for p in productsFound:
        productList.append({"id": p['p_id'], "name": p['p_name'], "brand": p['p_brand'], "desc": p['p_desc'],
                            "wifi": p['p_wifi'], "video_res": p['p_video_res'], "color": p['color'],
                            "img": p['p_img'], "stock": p['stock'], "cost": p['p_cost'], "price": p['p_price'],
                            "status": p['p_status']})
    return productList


# Find the specific product given the ID
def getsingleproductmodel(prodID):
    # TO BE ADDED BY STUDENTS
    return


def createNewProductModel(name, brand, video_res, wifi, color, price, cost, stock, img, status):
    # DB credentials found in backend_model/connectDB.py
    db = Dbconnect()
    query = "INSERT INTO products(p_name, p_brand, p_video_res, p_wifi, color, p_price, p_cost," \
            "stock, p_img, p_status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    db.execute(query, (name, brand, video_res, wifi, color, price, cost, stock, img, status))
    return
