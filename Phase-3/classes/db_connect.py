import pymysql
import pymysql.cursors
# Use this to access database
class DBConnect():
    def __init__(self) -> None:
        self.connection = pymysql.connect(host='sql9.freemysqlhosting.net',
                                          db='sql9607915',
                                          user='sql9607915',
                                          password='Sz7jbHnAwK',
                                          port=3306)
        self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        
    def query(self, sql, params=None):
        if params:
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)
            
        result = self.cursor.fetchall()
        return result

    def execute(self, sql, params=None):
        if params:
            print("Query parameters: ", params)
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)
        
        return self.cursor
    
    def commit(self):
        self.connection.commit()
        
    def rollback(self):
        self.connection.rollback()
        
