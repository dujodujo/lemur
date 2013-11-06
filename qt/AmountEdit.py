from Constants import*

class AmountEdit(QtGui.QLineEdit):
    def __init__(self, txt, parent=None):
        super(AmountEdit, self).__init__(parent)

        self.txt = txt
        #self.textChanged().connect(self.numbify)

    def paintEvent(self, QPaintEvent):
        QtGui.QLineEdit.paintEvent(self, QPaintEvent)
        if self.txt:
            panel = QtGui.QStyleOptionFrameV2()
            self.initStyleOption(panel)
            txtRect = self.style().subElementRect(QtGui.QStyle.SE_LineEditContents,
                panel, self)
            txtRect.adjust(2, 0, -10, 0)
            painter = QtGui.QPainter(self)
            painter.setPen(self.palette().brush(QtGui.QPalette.Disabled,
                QtGui.QPalette.Text).color())
            painter.drawText(txtRect, QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter,
                self.txt)

    def numbify(self):
        text = unicode(self.text()).strip()
        chars = '0123456789.'
        position = self.cursorPosition()
        string = ''.join([i for i in text if i in chars])
        if '.' in string:
            p = string.find('.')
            string = string.replace('.', '')
            string = string[:p]+'.'+string[p:]
        self.setText(string)
        self.setCursorPosition(position)