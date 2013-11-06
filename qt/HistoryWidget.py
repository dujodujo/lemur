from Constants import*

class HistoryWidget(QtGui.QTreeWidget):
    def __init__(self, parent):
        super(HistoryWidget, self).__init__(parent)
        self.setColumnCount(2)
        self.setHeaderLabel(['Amount', 'To/From', 'When'])
        self.setIndentation(0)

    def empty(self):
        self.clear()

    def append(self, address, amount, date):
        if address is None:
            address = 'Unknown'
        if amount is None:
            amount = 'Unknown'
        if date is None:
            date = 'Unknown'
        item = QtGui.QTreeWidget([amount, address, date])
        if amount < 0:
            item.setForeground(0, QtGui.QBrush(QtGui.QColor("#BC1E1E")))
        self.insertTopLevelItem(0, item)
