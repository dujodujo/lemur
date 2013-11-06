import sys
from PyQt4.QtGui import*
from PyQt4.QtCore import*

class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        layout = QVBoxLayout()
        okButton = QPushButton('ok')
        noButton = QPushButton('no')
        layout.addWidget(okButton)
        layout.addWidget(noButton)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = Dialog()
    frame.show()
    app.exec_()