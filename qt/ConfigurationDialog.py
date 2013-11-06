from PyQt4 import QtCore, QtGui, QtOpenGL
from OpenGL.GL import*
import sys, os, math, random, re

class ConfigurationDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(ConfigurationDialog, self).__init__(parent)

        self.contentsWidget = QtGui.QListWidget()
        self.contentsWidget.setViewMode(QtGui.QListWidget.IconMode)
        self.contentsWidget.setIconSize(QtCore.QSize(64, 64))
        self.contentsWidget.setMovement(QtGui.QListView.Static)
        self.contentsWidget.setMaximumWidth(128)
        self.contentsWidget.setSpacing(12)

        self.pageWidget = QtGui.QStackedWidget()
        self.pageWidget.addWidget(ConfigurationPage())
        self.pageWidget.addWidget(UpdatePage())
        self.pageWidget.addWidget(TabPage())
        self.pageWidget.addWidget(ImagePage())
        self.pageWidget.addWidget(PhotoPage())

        closeButton = QtGui.QPushButton('close')
        closeButton.clicked.connect(self.close)

        okButton = QtGui.QPushButton('ok')
        okButton.clicked.connect(self.testOkButton)

        self.createIcons()
        self.contentsWidget.setCurrentRow(0)

        horLayout = QtGui.QHBoxLayout()
        horLayout.addWidget(self.contentsWidget)
        horLayout.addWidget(self.pageWidget, 1)

        buttonLayout = QtGui.QHBoxLayout()
        buttonLayout.addStretch(1)
        buttonLayout.addWidget(closeButton)
        buttonLayout.addWidget(okButton)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addStretch(1)
        mainLayout.addLayout(horLayout)
        mainLayout.addLayout(buttonLayout)

        self.setLayout(mainLayout)
        self.setWindowTitle('Configuration Dialog')
        self.show()

    def testOkButton(self):
        print('test ok button')

    def createIcons(self):
        icon = QtGui.QIcon(os.path.join(os.getcwd(), 'icons', 'btn.png'))
        buttons = ['config', 'update', 'tab', 'image', 'photo']
        for buttonName in buttons:
            button = QtGui.QListWidgetItem(self.contentsWidget)
            button.setIcon(icon)
            button.setText(buttonName)
        self.contentsWidget.currentItemChanged.connect(self.changePages)

    def changePages(self, current, last):
        if not current:
            current = last
        self.pageWidget.setCurrentIndex(self.contentsWidget.row(current))

class ConfigurationPage(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ConfigurationPage, self).__init__(parent)

        configGroup = QtGui.QGroupBox('Configuration')
        label = QtGui.QLabel('Label')

        layout = QtGui.QHBoxLayout()
        layout.addWidget(label)

        configLayout = QtGui.QVBoxLayout()
        configLayout.addLayout(layout)

        configGroup.setLayout(configLayout)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(configGroup)
        mainLayout.addStretch(1)

        self.setLayout(mainLayout)

class UpdatePage(QtGui.QWidget):
    def __init__(self, parent=None):
        super(UpdatePage, self).__init__(parent)

        #Update Group
        updateGroup = QtGui.QGroupBox('Package selection')

        systemCheckBox = QtGui.QCheckBox('Update system')
        applicationCheckBox = QtGui.QCheckBox('Update application')
        documentsCheckBox = QtGui.QCheckBox('Update documentation')

        #Package Group
        packageGroup = QtGui.QGroupBox('Existing packages')
        packageList = QtGui.QListWidget()

        qtItem = QtGui.QListWidgetItem(packageList)
        qtItem.setText('qt')
        qsItem = QtGui.QListWidgetItem(packageList)
        qsItem.setText('qs')
        qpItem = QtGui.QListWidgetItem(packageList)
        qpItem.setText('qp')

        updateButton = QtGui.QPushButton('start update')

        updateLayout = QtGui.QVBoxLayout()
        updateLayout.addWidget(systemCheckBox)
        updateLayout.addWidget(applicationCheckBox)
        updateLayout.addWidget(documentsCheckBox)
        updateGroup.setLayout(updateLayout)

        packageLayout = QtGui.QVBoxLayout()
        packageLayout.addWidget(packageList)
        packageGroup.setLayout(packageLayout)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(updateGroup)
        mainLayout.addWidget(packageGroup)
        mainLayout.addWidget(updateButton)
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)

class TabPage(QtGui.QWidget):
    def __init__(self, parent=None):
        super(TabPage, self).__init__(parent)

        #Tab Group
        tabGroup = QtGui.QGroupBox('Tab selection')

        tabWidget = QtGui.QTabWidget()
        tabWidget.addTab(GeneralTab(self), 'General')
        tabWidget.addTab(PermissionTab(self), 'Permission')
        tabWidget.addTab(ApplicationTab(self), 'Application')

        buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.close)

        tabLayout = QtGui.QVBoxLayout()
        tabLayout.addWidget(tabWidget)
        tabLayout.addWidget(buttonBox)
        tabGroup.setLayout(tabLayout)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(tabGroup)
        self.setLayout(mainLayout)

        self.setWindowTitle("Tab Dialog")

class GeneralTab(QtGui.QWidget):
    def __init__(self, parent=None):
        super(GeneralTab, self).__init__(parent)

        nameLabel = QtGui.QLabel('name')
        lineEdit = QtGui.QLineEdit()

        pathLabel = QtGui.QLabel('path')
        pathValueLabel = QtGui.QLineEdit()

        extensionLabel = QtGui.QLabel('extension')
        extensionValueLabel = QtGui.QLineEdit()

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(nameLabel)
        mainLayout.addWidget(lineEdit)
        mainLayout.addWidget(pathLabel)
        mainLayout.addWidget(pathValueLabel)
        mainLayout.addWidget(extensionLabel)
        mainLayout.addWidget(extensionValueLabel)
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)

class PermissionTab(QtGui.QWidget):
    def __init__(self, parent=None):
        super(PermissionTab, self).__init__(parent)

        permissionGroup = QtGui.QGroupBox('Permission')
        readBox = QtGui.QCheckBox('Read')
        readBox.setChecked(False)
        writeBox = QtGui.QCheckBox('Write')
        writeBox.setChecked(False)
        executableBox = QtGui.QCheckBox('Execute')
        executableBox.setChecked(False)

        ownerGroup = QtGui.QGroupBox('Ownership')
        ownerLabel = QtGui.QLabel('Owner')
        ownerValueLabel = QtGui.QLineEdit()
        groupLabel = QtGui.QLabel('Group')
        groupValueLabel = QtGui.QLineEdit()

        permissionLayout = QtGui.QVBoxLayout()
        permissionLayout.addWidget(readBox)
        permissionLayout.addWidget(writeBox)
        permissionLayout.addWidget(executableBox)
        permissionGroup.setLayout(permissionLayout)

        ownerLayout = QtGui.QVBoxLayout()
        ownerLayout.addWidget(ownerLabel)
        ownerLayout.addWidget(ownerValueLabel)
        ownerLayout.addWidget(groupLabel)
        ownerLayout.addWidget(groupValueLabel)
        ownerGroup.setLayout(ownerLayout)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(permissionGroup)
        mainLayout.addWidget(ownerGroup)
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)

class ApplicationTab(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ApplicationTab, self).__init__(parent)

        topLabel = QtGui.QLabel('Open')
        appsListBox = QtGui.QListWidget()
        apps = ['app %d' % i for i in range(30)]
        appsListBox.insertItems(0, apps)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(topLabel)
        mainLayout.addWidget(appsListBox)
        self.setLayout(mainLayout)

class ImagePage(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ImagePage, self).__init__(parent)

        self.renderArea = RenderArea()
        self.buttonLayout = self.createButtonsLayout()

        self.shapeComboBox = QtGui.QComboBox()
        self.shapeComboBox.addItem('Rectangle', RenderArea.rectangle)
        self.shapeComboBox.addItem('Pixmap', RenderArea.pixmap)
        self.shapeComboBox.addItem('Text', RenderArea.text)
        self.shapeComboBox.addItem('Ellipse', RenderArea.ellipse)

        shapeLabel = QtGui.QLabel('Shape:')
        shapeLabel.setBuddy(self.shapeComboBox)
        self.shapeComboBox.activated.connect(self.shapeChanged)

        mainLayout = QtGui.QGridLayout()
        mainLayout.addWidget(self.renderArea,0,0)
        mainLayout.addWidget(self.shapeComboBox,1,0)
        mainLayout.addLayout(self.buttonLayout,2,0,QtCore.Qt.AlignLeft)
        self.setLayout(mainLayout)

    def shapeChanged(self):
        shape = self.shapeComboBox.itemData(self.shapeComboBox.currentIndex())
        self.renderArea.setShape(shape)

    def createButtonsLayout(self):
        self.rectButton = self.createButton("rect", self.drawRect)
        self.ellipseButton = self.createButton("ellipse", self.drawEllipse)
        self.pixmapButton = self.createButton("pixmap", self.drawPixmap)

        buttonsLayout = QtGui.QHBoxLayout()
        buttonsLayout.addStretch()
        buttonsLayout.addWidget(self.rectButton)
        buttonsLayout.addWidget(self.ellipseButton)
        buttonsLayout.addWidget(self.pixmapButton)
        return buttonsLayout

    def drawRect(self):
        self.renderArea.setShape(RenderArea.rectangle)

    def drawEllipse(self):
        self.renderArea.setShape(RenderArea.ellipse)

    def drawPixmap(self):
        self.renderArea.setShape(RenderArea.pixmap)

    def createButton(self, text, member):
        button = QtGui.QPushButton(text)
        button.clicked.connect(member)
        return button

class RenderArea(QtGui.QWidget):
    rectangle, ellipse, pixmap, text = range(4)

    def __init__(self, parent=None):
        super(RenderArea, self).__init__(parent)

        self.pen = QtGui.QPen()
        self.brush = QtGui.QBrush()
        self.pixmap = QtGui.QPixmap()
        self.pixmap.load('sprocket.png')
        self.shape = RenderArea.pixmap

        self.setBackgroundRole(QtGui.QPalette.Base)
        self.setAutoFillBackground(True)

    def setShape(self, shape):
        self.shape = shape
        self.update()

    def setPen(self, pen):
        self.pen = pen
        self.update()

    def setBrush(self, brush):
        self.brush = brush
        self.update()

    def paintEvent(self, QPaintEvent):
        rect = QtCore.QRect(10, 20, 80, 60)

        QPaintEvent = QtGui.QPainter(self)
        QPaintEvent.setPen(self.pen)
        QPaintEvent.setBrush(self.brush)

        for x in range(0,self.width(),100):
            for y in range(0,self.height(),100):
                QPaintEvent.save()
                QPaintEvent.translate(x,y)

                if self.shape == RenderArea.rectangle:
                    QPaintEvent.drawRect(rect)
                elif self.shape == RenderArea.ellipse:
                    QPaintEvent.drawEllipse(rect)
                elif self.shape == RenderArea.text:
                    QPaintEvent.drawText(rect, QtCore.Qt.AlignCenter, 'QT')
                elif self.shape == RenderArea.pixmap:
                    QPaintEvent.drawPixmap(20,20,self.pixmap)
                QPaintEvent.restore()

class PhotoPage(QtGui.QWidget):
    def __init__(self, parent=None):
        super(PhotoPage, self).__init__(parent)

        self.createComponents()
        self.createConnects()
        self.createLayouts()

        self.currentDirectory = ''
        self.resize(600,600)
        self.setWindowTitle("Viewer")

    def createComponents(self):
        self.button = QtGui.QPushButton('push')
        self.editCurrentDirectory = QtGui.QLineEdit()
        self.view = QtGui.QGraphicsView()
        self.scene = QtGui.QGraphicsScene()
        self.view.setScene(self.scene)

    def createLayouts(self):
        layoutCentral = QtGui.QVBoxLayout()
        layoutHorizontal = QtGui.QHBoxLayout()
        layoutHorizontal.addWidget(self.button)
        layoutHorizontal.addWidget(self.editCurrentDirectory)

        layoutCentral.addLayout(layoutHorizontal)
        layoutCentral.addWidget(self.view)
        self.setLayout(layoutCentral)

    def createConnects(self):
        self.editCurrentDirectory.returnPressed.connect(self.loadPhotos)
        self.button.clicked.connect(self.fileBrowser)

    @QtCore.pyqtSlot()
    def loadPhotos(self):
        self.currentDirectory = unicode(self.editCurrentDirectory.text())
        self.photoBrowser = PhotoBrowser(self.currentDirectory, self)
        photoCount = self.photoBrowser.loadPhotos()
        self.view.setScene(self.photoBrowser)

    @QtCore.pyqtSlot()
    def fileBrowser(self):
        dialog = QtGui.QFileDialog(self, self.tr("Select Directory"),
            QtGui.QDesktopServices.storageLocation(
                QtGui.QDesktopServices.PicturesLocation))
        dialog.setFileMode(QtGui.QFileDialog.DirectoryOnly)
        if dialog.exec_():
            self.editCurrentDirectory.setText(unicode(dialog.selectedFiles()[0]))
            self.loadPhotos()

class PhotoBrowser(QtGui.QGraphicsScene):
    def __init__(self, directory, parent):
        super(PhotoBrowser, self).__init__(parent)

        self.directory = directory
        self.files = []
        self.pixmaps = []
        self.initFiles()

    def initFiles(self):
        files = os.listdir(self.directory)
        imageExtensions = re.compile("(?:[Jj][Pp][Ee]?[Gg]|[Pp][Nn][Gg])$")

        for fileName in files:
            if imageExtensions.search(fileName):
                self.files.append(fileName)
        self.files.sort()

    def loadPhotos(self):
        progress = QtGui.QProgressDialog(
            self.tr('Loading photos...'),
            self.tr('complete'),
            0,
            len(self.files),
            self.parent()
        )
        progress.setWindowModality(QtCore.Qt.WindowModal)

        i = 0
        y = 0
        for fileName in self.files:
            progress.setValue(i)
            filePath = os.path.join(self.directory,fileName)
            pixmap = QtGui.QPixmap(filePath)
            pixmap = pixmap.scaled(QtCore.QSize(250,250),QtCore.Qt.KeepAspectRatio)
            pixmapItem = self.addPixmap(pixmap)
            textItem = self.addSimpleText(fileName)
            textItem.setPos(QtCore.QPoint(pixmap.width(),y+pixmap.height()))
            pixmapItem.setPos(QtCore.QPointF(pixmap.width(),y))
            y += pixmap.height()+50

            if progress.wasCanceled():
                self.clear()
                break

        progress.setValue(len(self.files))
        return len(self.files)

    def mouseDoubleClickEvent(self, QGraphicsSceneMouseEvent):
        fileName = self.currentFileName()
        if fileName:
            filePath = os.path.join(self.directory, fileName)
            viewer = PhotoViewer(self.parent(), filePath)
            viewer.show()

    def currentFileName(self):
        if not self.selectedItems():
            return None
        else:
            return unicode(self.selectedItems()[0].data(0).toString())

class PhotoViewer(QtGui.QDialog):
    def __init__(self, image, parent=None):
        super(PhotoViewer, self).__init__(parent)

        self.setWindowTitle("Viewer")
        self.setMinimumSize(500,500)

        self.view = QtGui.QGraphicsView(self)
        self.pixmap = QtGui.QPixmap(image)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.view)
        self.setLayout(layout)

    def resizeEvent(self, QResizeEvent):
        self.scalePixmap()
        self.showPixmap()

    def scalePixmap(self):
        x = self.view.width()
        y = self.view.height()
        self.pixmap.scaled(QtCore.QSize(x,y), QtCore.Qt.KeepAspectRatio)

    def showPixmap(self):
        self.scene = QtGui.QGraphicsScene(self)
        self.scene.addPixmap(self.pixmap)
        self.view.setScene(self.scene)