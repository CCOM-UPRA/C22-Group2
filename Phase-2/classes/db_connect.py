import pymysql
# Use this to access database
class DBConnect(pymysql.connections.Connection):
    def __init__(self) -> None:
        super(DBConnect, self).__init__(host='sql9.freemysqlhosting.net',
                    db='sql9607915',
                    user='sql9607915',
                    password='Sz7jbHnAwK',
                    port=3306)