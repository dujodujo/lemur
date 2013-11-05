import sqlite3, os

class Database(object):
    def __init__(self, db_file="xsKontakti.db"):
        database_exists = os.path.exists(db_file)
        self.conn = sqlite3.connect(db_file)
        if not database_exists:
            self.create_db()

    def create_db(self):
        sql = """CREATE TABLE Kontakti
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
              ime TEXT,
              priimek TEXT,
              telStevilla TEXT,
              mail TEXT)
              """

        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()
        cursor.close()

    def modify_db(self,sql,t):
        cursor = self.conn.cursor()
        cursor.execute(sql,t)
        self.conn.commit()
        cursor.close()

    def get_db(self,sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        kontakti = cursor.fetchall()
        cursor.close()
        return kontakti