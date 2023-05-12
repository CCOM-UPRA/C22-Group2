from backend_model.reportsModel import *

def getDatedReport(date, filter, product_id = None):
    return getDatedReportModel(date, filter, product_id)

def getStockReport():
    return getStockReportModel()

def get_products_id():
    return getProductsIDModel()