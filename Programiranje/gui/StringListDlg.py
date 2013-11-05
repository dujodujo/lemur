import sys
from PyQt4.QtCore import*
from PyQt4.QtGui import*

class StringListDlg(QDialog):
    def __init__(self, name, vegetables = None, parent = None):
        super(StringListDlg, self).__init__(parent)
        self.name = name
        self.listWidget = QListWidget()
        if vegetables:
            self.listWidget.addItems(vegetables)
            self.listWidget.setCurrentRow(0)
        buttonLayout = QVBoxLayout()
        for text, slot in (("&Add", self.add),
                            ("&Remove", self.remove),
                            ("&Edit", self.edit),
                            ("&Up", self.up),
                            ("&Down", self.down),
                            ("&Sort", self.listWidget.sortItems),
                            ("&Close", self.accept)):
            button = QPushButton(text)
            button.setFocusPolicy(Qt.NoFocus)
            buttonLayout.addWidget(button)
            self.connect(button, SIGNAL("clicked()"), slot)
        layout = QHBoxLayout()
        layout.addWidget(self.listWidget)
        layout.addLayout(buttonLayout)
        self.setLayout(layout)
        self.setWindowTitle("Edit {} list".format(self.name))

    def add(self):
        row = self.listWidget.currentRow()
        title = "Add {}".format(self.name)
        string, ok = QInputDialog.getText(self, title, title)
        if string and ok:
            self.listWidget.insertItem(row, string)

    def remove(self):
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)
        if item is None:
            return
        reply = QMessageBox.question(self, "Remove {}".format(self.name),
            "Remove {} {}".format(self.name, item.text()),
            QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            item = self.listWidget.takeItem(row)
            del item

    def edit(self):
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)
        if item is not None:
            title = "Remove {}".format(item.text())
            string, ok = QInputDialog.getText(self, title, title, QLineEdit.Normal, item.text())
            if string and ok:
                item.setText(string)

    def up(self):
        row = self.listWidget.currentRow()
        if  row > 1:
            item = self.listWidget.takeItem(row)
            self.listWidget.insertItem(row - 1, item)
            self.listWidget.setCurrentItem(item)

    def down(self):
        row = self.listWidget.currentRow()
        if  row < self.listWidget.count() - 1:
            item = self.listWidget.takeItem(row)
            self.listWidget.insertItem(row + 1, item)
            self.listWidget.setCurrentItem(item)

    def reject(self):
        self.accept()

    def accept(self):
        self.vegetables = []
        for row in range(self.listWidget.count()):
            self.vegetables.append(self.listWidget.item(row).text())
        self.emit(SIGNAL("acceptedList(QStringList)"), self.vegetables)
        QDialog.accept(self)

if __name__ == "__main__":
    vegetables = ["Asparagus","Chickpeas","Soy beans","Broccoli","Cabbage",
              "Cauliflower","Celery","Garlic","Onion","Parsley","Peppers",
              "Carrot","Radish","Paprika","Pumpkin","Potato","Yam"]
    app = QApplication([])
    form = StringListDlg("Vegetables", vegetables)
    form.exec_()