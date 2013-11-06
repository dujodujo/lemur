from Constants import*

class IconSpinBox(QtGui.QSpinBox):
    def __init__(self):
        super(IconSpinBox, self).__init__()

class ImageDelegate(QtGui.QItemDelegate):
    def __init__(self):
        super(ImageDelegate, self).__init__()

    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex):
        comboBox = QtGui.QComboBox(QWidget)
        if QModelIndex.column() == 1:
            comboBox.addItem('Normal')
            comboBox.addItem('Active')
            comboBox.addItem('Disabled')
            comboBox.addItem('Selected')
        elif QModelIndex.column() == 2:
            comboBox.addItem('Off')
            comboBox.addItem('On')
        comboBox.activated.connect(self.commit)
        return comboBox

    def setEditorData(self, QWidget, QModelIndex):
        comboBox = QWidget
        if not comboBox: return
        position = comboBox.findText(QModelIndex.model().data(QModelIndex),
            QtCore.Qt.MatchExactly)
        comboBox.setCurrentIndex(position)

    def setModelData(self, QWidget, QAbstractItemModel, QModelIndex):
        comboBox = QWidget
        if not comboBox: return
        QAbstractItemModel.setData(QModelIndex, comboBox.currentText())

    def commit(self):
        self.commitData.emit(self.sender())

class IconPreviewArea(QtGui.QWidget):
    def __init__(self, parent=None):
        super(IconPreviewArea, self).__init__(parent)

        mainLayout = QtGui.QGridLayout()
        self.setLayout(mainLayout)

        self.stateLabels = []
        self.modelLabels = []
        self.pixmapLabels = []

        self.icon = QtGui.QIcon()
        self.size = QtCore.QSize()

        self.stateLabels.append(self.createHeaderLabel('Off'))
        self.stateLabels.append(self.createHeaderLabel('On'))

        self.modelLabels.append(self.createHeaderLabel('Normal'))
        self.modelLabels.append(self.createHeaderLabel('Active'))
        self.modelLabels.append(self.createHeaderLabel('Disabled'))
        self.modelLabels.append(self.createHeaderLabel('Selected'))

        for j, label in enumerate(self.stateLabels):
            mainLayout.addWidget(label, j+1, 0)
        for i, label in enumerate(self.modelLabels):
            mainLayout.addWidget(label, 0, i+1)
            self.pixmapLabels.append([])
            for j in range(len(self.stateLabels)):
                self.pixmapLabels[i].append(self.createPixmapLabel())
                mainLayout.addWidget(self.pixmapLabels[i][j], j+1, i+1)

    def setIcon(self, icon):
        self.icon = icon
        self.updatePixmapLabels()

    def setSize(self, size):
        if self.size != size:
            self.size = size
            self.updatePixmapLabels()

    def createHeaderLabel(self, txt):
        label = QtGui.QLabel('<b>%s</b>' % txt)
        label.setAlignment(QtCore.Qt.AlignCenter)
        return label

    def createPixmapLabel(self):
        label = QtGui.QLabel()
        label.setEnabled(False)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setFrameShape(QtGui.QFrame.Box)
        label.setSizePolicy(QtGui.QSizePolicy.Expanding,
                            QtGui.QSizePolicy.Expanding)
        label.setBackgroundRole(QtGui.QPalette.Base)
        label.setAutoFillBackground(True)
        label.setMinimumSize(132, 132)
        return label

    def updatePixmapLabels(self):
        for i in range(len(self.modelLabels)):
            if i == 0:
                mode = QtGui.QIcon.Normal
            elif i == 1:
                mode = QtGui.QIcon.Active
            elif i == 2:
                mode = QtGui.QIcon.Disabled
            elif i == 3:
                mode = QtGui.QIcon.Selected
            elif i == 4:
                mode = QtGui.QIcon.On
            elif i == 5:
                mode = QtGui.QIcon.Off
            for j in range(len(self.stateLabels)):
                state = {True: QtGui.QIcon.Off, False: QtGui.QIcon.On}[j==0]
                pixmap = self.icon.pixmap(self.size, mode, state)
                self.pixmapLabels[i][j].setPixmap(pixmap)
                self.pixmapLabels[i][j].setEnabled(not pixmap.isNull())

    def mouseMoveEvent(self, QMouseEvent):
        #widgetPosition = self.mapFromGlobal(QMouseEvent.globalPos())
        text = QtCore.QString('text')
        QtGui.QToolTip.showText(QMouseEvent.globalPos(), text, self)

class LineEdit(QtGui.QLineEdit):
    def __init__(self, parent=None):
        super(LineEdit, self).__init__(parent)

        self.value = 10
        string = QtCore.QString(str(self.value))
        self.setText(string)

    def setValue(self):
        self.value += 1
        string = QtCore.QString(str(self.value))
        self.setText(string)

class SlidersGroupBox(QtGui.QGroupBox):
    vc = QtCore.pyqtSignal(int)
    def __init__(self, orientation, title, parent=None):
        super(SlidersGroupBox, self).__init__(title, parent)

        self.scrollBar = QtGui.QScrollBar(QtCore.Qt.Horizontal)
        self.scrollBar.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.scrollBar.setValue(10)
        self.scrollBar.setRange(0, 100)

        self.scrollBar.valueChanged.connect(self.scrollBar.setValue)
        self.scrollBar.valueChanged.connect(self.vc)

        self.createControls('Controls')

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.scrollBar)
        layout.addWidget(self.controlGroupBox)
        self.setLayout(layout)

    def setValue(self, value):
        self.scrollBar.setValue(value)

    def setMinimum(self, value):
        self.dial.setMinimum(value)

    def setMaximum(self, value):
        self.dial.setMaximum(value)

    def createControls(self, title):
        self.controlGroupBox = QtGui.QGroupBox(title)

        self.valueSpinLabel = QtGui.QLabel('Current value')
        self.valueSpinBox = QtGui.QSpinBox()
        self.valueSpinBox.setRange(-100, 100)
        self.valueSpinBox.setSingleStep(1)

        self.valueLabel = QtGui.QLabel('Current value')
        #self.valueBox = QtGui.QLineEdit()
        self.valueLineEdit = LineEdit()

        controlLayout = QtGui.QVBoxLayout()

        controlLayoutSpin = QtGui.QHBoxLayout()
        controlLayoutSpin.addWidget(self.valueSpinLabel)
        controlLayoutSpin.addWidget(self.valueSpinBox)

        controlLayoutLabel = QtGui.QHBoxLayout()
        controlLayoutLabel.addWidget(self.valueLabel)
        controlLayoutLabel.addWidget(self.valueLineEdit)

        controlLayout.addLayout(controlLayoutLabel)
        controlLayout.addLayout(controlLayoutSpin)
        self.controlGroupBox.setLayout(controlLayout)

class WindowDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(WindowDialog, self).__init__(parent)

        self.centralWidget = QtGui.QWidget()
        self.mainLayout = QtGui.QGridLayout()

        self.createPreviewGroupBox()
        self.createImageGroupBox()
        self.createSliderGroupBox()
        self.createActions()
        self.createLayout()
        self.createMenu()

        self.setWindowTitle('icons')
        self.centralWidget.show()

    def createSliderGroupBox(self):
        self.sliderGroupBox = SlidersGroupBox(QtCore.Qt.Vertical, 'Sliders')
        self.sliderGroupBox.valueSpinBox.setValue(12)
        self.sliderGroupBox.vc.connect(self.sliderGroupBox.valueSpinBox.setValue)
        self.sliderGroupBox.vc.connect(self.sliderGroupBox.valueLineEdit.setValue)
        #self.sliderGroupBox.vc.connect(self.sliderGroupBox.setValue)

    def createPreviewGroupBox(self):
        self.previewGroupBox = QtGui.QGroupBox('Preview')
        self.previewArea = IconPreviewArea()

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.previewArea)
        self.previewGroupBox.setLayout(layout)

    def createImageGroupBox(self):
        self.imageGroupBox = QtGui.QGroupBox('Images')

        self.imagesTable = QtGui.QTableWidget()
        self.imagesTable.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        #self.imagesTable.setItemDelegate(ImageDelegate())

        self.imagesTable.horizontalHeader().setDefaultSectionSize(90)
        self.imagesTable.setColumnCount(3)
        self.imagesTable.setHorizontalHeaderLabels(('Image', 'Mode', 'State'))
        self.imagesTable.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Stretch)
        self.imagesTable.horizontalHeader().setResizeMode(1, QtGui.QHeaderView.Fixed)
        self.imagesTable.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Fixed)
        self.imagesTable.verticalHeader().hide()

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.imagesTable)
        self.imageGroupBox.setLayout(layout)

    def createActions(self):
        self.addImageAction = QtGui.QAction('Add Image', self,
            triggered=self.addImage)
        self.removeImageAction = QtGui.QAction('Remove Image', self,
            triggered=self.removeAllImages)
        self.exitAction = QtGui.QAction('Quit', self,
            triggered=self.close)

    def createLayout(self):
        self.mainLayout = QtGui.QGridLayout()
        self.mainLayout.addWidget(self.previewGroupBox, 0, 0, 1, 2)
        self.mainLayout.addWidget(self.imageGroupBox, 1, 0)
        self.mainLayout.addWidget(self.sliderGroupBox, 0, 3)
        self.setLayout(self.mainLayout)
        self.centralWidget.setLayout(self.mainLayout)

    def createMenu(self):
        self.menuBar = QtGui.QMenuBar()
        menu = self.menuBar.addMenu('File')
        menu.addAction(self.addImageAction)
        menu.addAction(self.removeImageAction)
        menu.addAction(self.exitAction)
        menu.addSeparator()
        self.mainLayout.setMenuBar(self.menuBar)

    def createContexMenu(self):
        self.imagesTable.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.imagesTable.addAction(self.addImageAction)
        self.imagesTable.addAction(self.removeImageAction)

    def about(self):
        QtGui.QMessageBox.about(self, 'About icons', 'About')

    def addImage(self):
        fileNames = QtGui.QFileDialog.getOpenFileNames(self,
            'Open Images', os.path.join(os.getcwd(), 'images'))
        for fileName in fileNames:
            row = self.imagesTable.rowCount()
            self.imagesTable.setRowCount(row+1)
            imageName = QtCore.QFileInfo(fileName).baseName()

            item0 = QtGui.QTableWidgetItem(imageName)
            item1 = QtGui.QTableWidgetItem('Normal')
            item2 = QtGui.QTableWidgetItem('Off')

            self.imagesTable.setItem(row, 0, item0)
            self.imagesTable.setItem(row, 1, item1)
            self.imagesTable.setItem(row, 2, item2)
            self.imagesTable.openPersistentEditor(item1)
            self.imagesTable.openPersistentEditor(item2)

    def removeImage(self):
        pass

    def removeAllImages(self):
        self.imagesTable.setRowCount(0)
        self.changeIcon()

    def changeIcon(self):
        icon = QtGui.QIcon()
        for row in range(self.imagesTable.rowCount()):
            item0 = self.imagesTable.item(row, 0)
            item1 = self.imagesTable.item(row, 1)
            item2 = self.imagesTable.item(row, 2)

            fileName = item0.data(QtCore.Qt.UserRole)
            image = QtGui.QImage(fileName)
            if not image.isNull():
                icon.addPixmap(QtGui.QPixmap.fromImage(image))
        self.previewArea.setIcon(icon)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    dialog = WindowDialog()
    app.exec_()