import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.spin_principal = QDoubleSpinBox()
        self.spin_principal.setRange(100,1000000)
        self.spin_principal.setValue(1000)
        self.spin_rate = QDoubleSpinBox()
        self.spin_rate.setRange(1,20)
        self.spin_rate.setValue(5)
        self.yearsComboBox = QComboBox()
        self.yearsComboBox.addItem("1 Year")
        self.yearsComboBox.addItems(["{}".format(y) for y in range(2,31)])
        self.toLabel = QLabel()

        self.label_principal = QLabel("Principal:")
        self.label_rate = QLabel("Rate:")
        self.label_year = QLabel("Year:")
        self.label_amount = QLabel("Amount:")

        grid = QGridLayout()
        grid.addWidget(self.label_principal,0,0)
        grid.addWidget(self.spin_principal,0,1)
        grid.addWidget(self.label_rate,1,0)
        grid.addWidget(self.spin_rate,1,1)
        grid.addWidget(self.label_year,2,0)
        grid.addWidget(self.yearsComboBox,2,1)
        grid.addWidget(self.toLabel,3,1)
        self.setLayout(grid)

        self.connect(self.spin_principal, SIGNAL("valueChanged(double)"), self.update_ui)
        self.connect(self.spin_rate, SIGNAL("valueChanged(double)"), self.update_ui)
        self.connect(self.yearsComboBox, SIGNAL("currentIndexChanged(int)"),self.update_ui)

        self.setWindowTitle("Interest")
        self.update_ui()

    def update_ui(self):
        principal = self.spin_principal.value()
        rate = self.spin_rate.value()
        year = self.yearsComboBox.currentIndex() + 1
        amount =  principal * ((1 + ( rate / 100.0)) ** year)
        self.toLabel.setText("$ {0:0.2f}".format(amount))

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()