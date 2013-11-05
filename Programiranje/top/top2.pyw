from PyQt4 import QtCore, QtGui
import math
import PyQt4.uic
app = QtGui.QApplication([])

class Top:
   def __init__(self):
        self.dlg = PyQt4.uic.loadUi("top.ui")
#        QtCore.QObject.connect(self.dlg.btIzracun, QtCore.SIGNAL("clicked()"), self.izracun)
        self.dlg.show()

#   def izracun(self):
#        hitrost = float(self.dlg.leHitrost.text())
#        kot = float(self.dlg.leKot.text())
#        razdalja = hitrost**2*math.sin(2*math.radians(kot))/9.81
#        self.dlg.lbIzracun.setText("Krogla bo preletela %.2f metrov" % razdalja)

top = Top()
app.exec_()
