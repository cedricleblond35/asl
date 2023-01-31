import mysql.connector

#https://pynative.com/python-mysql-database-connection/
# https://pynative.com/python-mysql-select-query-to-fetch-data/

# from mysql.connector import Error

# pip3 install mysql-connector
# https://dev.mysql.com/doc/connector-python/en/connector-python-reference.html

class dbQuery():
    def __init__(self):
        self.connection = self.connectionDB()

    def cursor(self):
        return self.connection.cursor()

    def query(self, sql, args):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql, args)

        except mysql.connector.Error as e:
            print("Error code:", e.errno)         # error number
            print("SQLSTATE value:", e.sqlstate) # SQLSTATE value
            print("Error message:", e.msg)       # error message
            print("Error:", e)                   # errno, sqlstate, msg values
            s = str(e)
            print("Error:", s)                   # errno, sqlstate, msg values
            
        
        return cursor

    def insert(self, sql, args):
        cursor = self.query(sql, args)
        id = cursor.lastrowid
        self.connection.commit()
        cursor.close()
        return id

    # https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-executemany.html
    def insertmany(self, sql, args):
        cursor = self.connection.cursor()
        cursor.executemany(sql, args)
        rowcount = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return rowcount

    def update(self, sql, args):
        cursor = self.query(sql, args)
        rowcount = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return rowcount

    def fetch(self, sql, args = ""):
        rows = []
        cursor = self.query(sql, args)
        if cursor.with_rows:
            rows = cursor.fetchall()
        cursor.close()
        return rows

    def fetchone(self, r):
        cursor = self.connection.cursor()
        cursor.execute(r)
        row = cursor.fetchone()
        cursor.close()
        print(row)
        return row
    
    def delete(self, sql, args):
        cursor = self.query(sql, args)
        rowcount = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return rowcount
        

    def connectionDB(self):
        try:
            return mysql.connector.connect(
            host="0.0.0.0",
            port=3310,
            user="root",
            passwd="MYsql",
            database="ASL")

        except mysql.connector.Error as e:
            print("Error code:", e.errno)         # error number
            print("SQLSTATE value:", e.sqlstate) # SQLSTATE value
            print("Error message:", e.msg)       # error message
            print("Error:", e)                   # errno, sqlstate, msg values
            s = str(e)
            print("Error:", s)                   # errno, sqlstate, msg values
    
    def __del__(self):
        self.connection.close()