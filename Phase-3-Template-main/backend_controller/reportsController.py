from backend_model.reportsModel import *


def getReport(timeframe, start_date, end_date, product):
    if timeframe == 'Day':
        query = "SELECT orders.order_id, p_name, p_brand, order_date, contains.p_price, product_quantity, p_total_price, " \
                "p_cost FROM orders JOIN contains JOIN products WHERE orders.order_id = contains.order_id AND " \
                "contains.p_id = products.p_id AND order_date = %s AND p_name = %s"
    else:
        query = "SELECT orders.order_id, p_name, p_brand, order_date, contains.p_price, product_quantity, p_total_price, p_cost " \
                "FROM orders JOIN contains JOIN products WHERE orders.order_id = contains.order_id AND contains.p_id = products.p_id " \
                "AND order_date BETWEEN %s AND %s AND p_name = %s"
    return getReportModel(timeframe, query, start_date, end_date, product)


def getNames():
    return getNamesModel()


def getDatedReport():
    return getDatedReportModel()


def getStockReport():
    return getStockReportModel()
