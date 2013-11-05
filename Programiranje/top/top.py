from PyQt4 import QtCore, QtGui, uic
app = QtGui.QApplication([])
dlg = uic.loadUi("top.ui")
print(dlg)