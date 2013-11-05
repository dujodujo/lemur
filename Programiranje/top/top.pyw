import math

from PyQt4 import QtCore, QtGui
import PyQt4.uic

app = QtGui.QApplication([])
dlg = PyQt4.uic.loadUi("top.ui")

def izracun():
    hitrost = float(dlg.leHitrost.text())
    kot = float(dlg.leKot.text())
    razdalja = hitrost**2*math.sin(2*math.radians(kot))/9.81
    dlg.lbIzracun.setText("krogla {}".format(razdalja))

    QtCore.QObject.connect(dlg.btIzracun, QtCore.SIGNAL("clicked()"),izracun())

dlg.show()
app.exec_()
