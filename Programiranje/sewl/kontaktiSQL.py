from PyQt4 import QtGui, QtCore, uic
#from sewl.database import Database
import sqlite3, os

class Kontakti(object):
    def __init__(self):
        self.dlg = uic.loadUi("kontakti.ui")
        self.db = Database()
        QtCore.QObject.connect(self.dlg.btIsci, QtCore.SIGNAL("clicked()"), self.isci)
        QtCore.QObject.connect(self.dlg.btShrani, QtCore.SIGNAL("clicked()"), self.shrani)
        QtCore.QObject.connect(self.dlg.btPobrisi, QtCore.SIGNAL("clicked()"), self.pobrisi)
        QtCore.QObject.connect(self.dlg.btSprazni, QtCore.SIGNAL("clicked()"), self.nastavi)
        self.dlg.show()

    def vnosi(self):
        return  [self.dlg.leIme.text(), self.dlg.lePriimek.text(),
                self.dlg.leTelefon.text(), self.dlg.leNaslov.text()]

    def isci(self):
        i_ime, i_priimek, i_telefon, i_naslov = self.vnosi()
        sql = 'SELECT ime, priimek, telStevilka, mail FROM Kontakti'
        kontakti = self.db.get_db(sql)
        for ime, priimek, telStevilka, mail in kontakti:
            if i_ime in ime:
                self.nastavi(ime, priimek, telStevilka, mail)
                break

    def shrani(self):
        i_ime, i_priimek, i_telefon, i_naslov = self.vnosi()
        sql = 'SELECT ime, priimek FROM Kontakti'
        kontakti = self.db.get_db(sql)
        for oseba in kontakti:
            if i_ime == oseba[0] and i_priimek == oseba[1]:
                t = (i_telefon,i_ime,i_priimek)
                sql = 'UPDATE Kontakti SET telStevilka=? WHERE ime=?, priimek=?'
                self.db.modify_db(sql,t)
                break
        else:
            t = (i_ime, i_priimek, i_telefon, i_naslov,)
            sql = 'INSERT into Kontakti (ime, priimek, telStevilka, mail) \
                  VALUES (?, ?, ?, ?)'
            self.db.modify_db(sql,t)

    def pobrisi(self):
        oseba = self.vnosi()
        i_ime = oseba[0]
        t=(i_ime,)
        sql = "DELETE FROM Kontakti WHERE ime=?"
        self.db.modify_db(sql,t)


    def nastavi(self, ime="", priimek="", telefon="", naslov=""):
        self.dlg.leIme.setText(ime)
        self.dlg.lePriimek.setText(priimek)
        self.dlg.leTelefon.setText(telefon)
        self.dlg.leNaslov.setText(naslov)

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
              telStevilka TEXT,
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

app = QtGui.QApplication([])
k = Kontakti()
app.exec_()




