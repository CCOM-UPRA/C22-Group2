import pymysql

# This is our simulation of the database
# We have two products here.
# The students must create their own productList when working on their eCommerce site
# Product images are loaded into static/images/product-images/
# Done in array instead of dictionaries to portray the differences
productList = [['1', "Tello Drone", 'DJI', 'desc here', 'Yes', '480p', 'White', 'dji_tello.jpg', '15', 'active', '89', '89'],
               ['2', 'Bebop 2', 'Parrot', 'desc', 'Yes', '1080p', 'Red', 'parrot_bebop_2.jpg', '3', 'active', '270', '290']]


def getProductsModel():
    productList = []
    conn = pymysql.connect(host='sql9.freemysqlhosting.net', db='sql9602731',
                           user='sql9602731', password='zChRVJs2Nf', port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * from products WHERE p_status = 'active'")
    results = cur.fetchall()
    for res in results:
        productList.append({"id": res[0], "name": res[1], "brand": res[2], "desc": res[3],
                    "wifi": res[4], "video_res": res[5], "color": res[6], "img": res[7],
                    "stock": res[8], "cost": res[9], "price": res[10], "status": res[11]})
    return productList


def getBrandsModel():
    # Simulating grabbing these filters via SQL from the database
    brands = ["DJI", "Ruko", "Parrot"]
    return brands

def getColorsModel():
    colors = ["White", "Gray", "Red"]
    return colors


def getVideoResModel():
    videores = ["480p", "1080p", "4k"]
    return videores


def getWifiModel():
    wifi = ['Yes', 'No']
    return wifi
