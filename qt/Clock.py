import sys, re, os, time
from PyQt4 import QtCore, QtGui

class Clock(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Clock, self).__init__(parent)

        self.value = 10
        self.timer = QtCore.QTimer(self)

    def startClock(self):
        self.timer.timeout.connect(self.singleUpdate)
        self.timer.start(1000)

    def singleUpdate(self):
        if self.value:
            self.value -= 1
            print(self.value)
            if self.value == 0:
                self.value = None
                return True
            return False

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    clock = Clock()
    sys.exit(app.exec_())
