import sys, os

from PySide.QtGui import*
from PySide.QtCore import*

class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.menuBar = QMenuBar()
        self.menu = self.menuBar.addMenu('Coins')
        self.createActions()

        layout = QVBoxLayout()

        self.okButton = QPushButton('ok')
        self.noButton = QPushButton('no')
        self.aboutButton = QPushButton('about')
        self.textValue = 0
        self.textEdit = QTextEdit()

        horLayout = QHBoxLayout()
        self.plusButton = QPushButton('plus')
        self.minusButton = QPushButton('minus')
        horLayout.addWidget(self.plusButton)
        horLayout.addWidget(self.minusButton)

        self.aboutButton.clicked.connect(self.about)
        self.noButton.clicked.connect(self.close)
        self.plusButton.clicked.connect(self.plus)
        self.minusButton.clicked.connect(self.minus)

        layout.addWidget(self.okButton)
        layout.addWidget(self.noButton)
        layout.addWidget(self.aboutButton)
        layout.addLayout(horLayout)
        layout.addWidget(self.textEdit)
        layout.setMenuBar(self.menuBar)
        self.setLayout(layout)

    def about(self):
        QMessageBox.about(self, 'About PySide', 'PySide')

    def plus(self):
        self.textValue += 1
        self.textEdit.setText(str(self.textValue))

    def minus(self):
        if self.textValue > 0:
            self.textValue -= 1
        self.textEdit.setText(str(self.textValue))

    def createActions(self):
        self.showAction = self.menu.addAction('Show')
        self.aboutAction = self.menu.addAction('About')
        self.closeAction = self.menu.addAction('Close')

        self.showAction.setStatusTip('show')
        self.aboutAction.setStatusTip('about')
        self.closeAction.setStatusTip('close')


        self.showAction.triggered.connect(self.plus)
        self.aboutAction.triggered.connect(self.about)
        self.closeAction.triggered.connect(self.close)

        icon = QIcon(os.path.join(os.getcwd(), 'icons', 'coin.png'))
        self.showAction.setIcon(icon)
        self.aboutAction.setIcon(icon)
        self.closeAction.setIcon(icon)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = Dialog()
    frame.show()
    app.exec_()