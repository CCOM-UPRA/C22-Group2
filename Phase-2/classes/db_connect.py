import pymysql
# Use this to access database
class DBConnect():
    def __init__(self) -> None:
        self.conn = pymysql.connections.Connection(host='sql9.freemysqlhosting.net',
                    db='sql9607915',
                    user='sql9607915',
                    password='Sz7jbHnAwK',
                    port=3306)