import sys, os, random
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):

    def __init__(self,parent = None):
        super(Form, self).__init__(parent)

        self.get_data()
        self.answers = 0
        self.count = 0

        self.countryLabel = QLabel("Country:")
        self.fromCountryLabel = QLabel()
        self.fromCountryLabel.setText("Slovenija")
        self.capitalLabel = QLabel("Capital:")
        self.fromLineEdit = QLineEdit()
        self.countLabel = QLabel()
        self.resultLabel = QLabel()

        grid = QGridLayout()
        grid.addWidget(self.countryLabel,0,0)
        grid.addWidget(self.fromCountryLabel,0,1)
        grid.addWidget(self.capitalLabel,1,0)
        grid.addWidget(self.fromLineEdit,1,1)
        grid.addWidget(self.countLabel,2,0)
        grid.addWidget(self.resultLabel,2,1)
        self.setLayout(grid)

        self.connect(self.fromLineEdit, SIGNAL("returnPressed()"), self.update_ui)

    def select(self):
        self.fromCountryLabel.setText(random.choice([x for x in self.capitals.keys()]))

    def update_ui(self):
        capitals = self.capitals
        country = self.fromCountryLabel.text()
        name = self.fromLineEdit.text()
        if name == capitals[country]:
            self.resultLabel.setText("Pravilno")
            self.count +=1
        else:
            self.resultLabel.setText("Nepravilno, pravilni odgovor je " + capitals[country] )
        self.answers +=1
        self.countLabel.setText("{}/{}".format(self.count,self.answers))
        self.fromLineEdit.clear()
        self.select()

    def get_data(self):
        self.capitals = {}
        if os.path.exists(os.getcwd() + "\\imena.txt"):
            for line in open("imena.txt", "rt"):
                line = line.strip()
                data = line.split(", ")
                country = data[0]
                capital = data[1]
                self.capitals[country] = capital

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
