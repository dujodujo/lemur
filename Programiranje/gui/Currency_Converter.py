import sys
import urllib
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        date = self.get_data()
        exchange_rate = sorted(self.exchange_rate.keys())

        dateLabel = QLabel(date)
        self.fromComboBox = QComboBox()
        self.fromComboBox.addItems(exchange_rate)
        self.fromSpinBox = QDoubleSpinBox()
        self.fromSpinBox.setRange(0.01,1000000.00)
        self.fromSpinBox.setValue(1.00)
        self.toComboBox = QComboBox()
        self.toComboBox.addItems(exchange_rate)
        self.toLabel = QLabel("1.00")

        grid = QGridLayout()
        grid.addWidget(dateLabel,0,0)
        grid.addWidget(self.fromComboBox,1,0)
        grid.addWidget(self.fromSpinBox,1,1)
        grid.addWidget(self.toComboBox,2,0)
        grid.addWidget(self.toLabel,2,1)
        self.setLayout(grid)

        self.connect(self.fromComboBox, SIGNAL("currentIndexChanged(int)"),self.update_ui)
        self.connect(self.toComboBox, SIGNAL("currentIndexChanged(int)"),self.update_ui)
        self.connect(self.fromSpinBox, SIGNAL("valueChanged(double)"),self.update_ui)
        self.setWindowTitle("Currency Converter")

    def update_ui(self):
        currency = self.toComboBox.currentText()

    def get_data(self):
        self.exchange_rate = {}
        try:
            date = "Unknown"
            socket = urllib.urlopen("http://www.nlb.si/?a=tecajnica&type=individuals&format=txt&date")
            for line in socket:
                line = line.decode("utf-8")
                if line.startswith("001"):
                    try:
                        line = line.strip()
                        data = line.split(" ")

                        ymd = data[1]
                        date = str(ymd[6:8] + "." + ymd[4:6] + "." + ymd[:4])

                        currency = data[5]
                        value = data[6].replace(",",".")
                        value = float(value)
                        self.exchange_rate[currency] = value
                        self.exchange_rate["EUR"] = 1.00
                    except ValueError:
                        pass
            return "Date {}".format(date)
        except Exception as e:
            return "Connection failed {}".format(e)

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()