import sys, re, os, time
from PyQt4 import QtCore, QtGui
import Gui
from Gui import*

class Timer(QtCore.QThread):
    def run(self):
        while True:
            self.emit(QtCore.SIGNAL('timer signal'))
            time.sleep(0.5)

class PasswordDialog(QtGui.QDialog):
    def __init__(self, parent):
        super(PasswordDialog, self).__init__(parent)

        self.setModal(True)
        self.passwordInput = QtGui.QLineEdit()
        self.passwordInput.setEchoMode(QtGui.QLineEdit.Password)

        self.createLayouts()

    def createLayouts(self):
        message = 'Enter password'

        self.mainLayout = QtGui.QVBoxLayout()
        self.mainLayout.addWidget(QtGui.QLabel(self.message))

        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(4)
        self.grid.addWidget(QtGui.QLabel, 1, 0)
        self.grid.addWidget(self.passwordInput, 1, 1)

        self.mainLayout.addLayout(self.grid)
        buttonLayout = self.createButtonsLayout(self)
        self.mainLayout.addLayout(buttonLayout)

        self.setLayout(self.mainLayout)

    def createButtonsLayout(self, dialog):
        buttonLayout = QtGui.QHBoxLayout()
        buttonLayout.addStretch(1)

        okButton = QtGui.QPushButton('Ok')
        buttonLayout.addWidget(okButton)
        okButton.clicked.connect(dialog.accept)

        noButton = QtGui.QPushButton('No')
        buttonLayout.addWidget(noButton)
        noButton.clicked.connect(dialog.reject)

        return buttonLayout

class TransactionWindow(QtGui.QDialog):
    def __init__(self, transId, parent):
        super(TransactionWindow, self).__init__()

        self.transId = transId
        self.parent = parent
        self.setModal(True)
        self.resize(100, 100)
        self.setWindowTitle('Transaction sent')

        self.layout = QtGui.QGridLayout(self)

        historyLabel = 'transaction sent'
        self.layout.addWidget(QtGui.QLabel(historyLabel))

        self.editLabel = QtGui.QLineEdit()
        self.editLabel.setPlaceholderText('transaction label')
        self.editLabel.setObjectName('label input')
        self.editLabel.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.layout.addWidget(self.editLabel)

        self.saveButton = QtGui.QPushButton('Save')
        self.layout.addWidget(self.saveButton)
        #self.saveButton.clicked.connect(self.setLabel)

        self.exec_()

    def setLabel(self):
        label = unicode(self.editLabel)
        self.parent.wallet.labels[self.transId] = label
        #super(TransactionWindow, self).accept()

class ReceivePopup(QtGui.QDialog):
    def __init__(self):
        pass

    def leaveEvent(self, event):
        self.close()

    def setup(self, address):
        label = QtGui.QLabel('Coin address')
        addressDisplay = QtGui.QLineEdit(address)
        addressDisplay.setReadOnly(True)

        mainLayout = QtGui.QVBoxLayout(self)
        mainLayout.addWidget(label)
        mainLayout.addWidget(addressDisplay)

        self.setMouseTracking(True)
        self.setWindowTitle('Coin')
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        self.layout().setSizeConstraint(QtGui.QLayout.SetFixedSize)

    def popup(self):
        parent = self.parent()
        position = parent.mapToGlobal(parent.rect().bottomLeft())
        self.move(position)
        mousePosition = self.mapToGlobal(self.rect().center())
        QtGui.QCursor.setPos(mousePosition)
        self.show()

class BalanceLabel(QtGui.QLabel):
    SHOW_CONNECTING = 1
    SHOW_BALANCE = 2
    SHOW_AMOUNT = 3

    def __init__(self, changeCurrency, parent=None):
        super(QtGui.QLabel, self).__init__('Connecting...', parent=None)

        self.changeCurrency = changeCurrency
        self.state = self.SHOW_CONNECTING
        self.balance = ''
        self.amount = ''

    def mousePressEvent(self, QMouseEvent):
        if self.state != self.SHOW_CONNECTING:
            self.changeCurrency(QMouseEvent.button() == QtCore.Qt.LeftButton)

    def setBalance(self, balance):
        self.balance = balance + ' reformat txt'
        if self.state == self.SHOW_AMOUNT:
            self.setText(self.balance)

    def setAmount(self, amount):
        self.amount = amount + ' reformat txt'
        if self.state == self.SHOW_AMOUNT:
            self.setText(self.amount)

    def showBalance(self):
        if self.state == self.SHOW_AMOUNT:
            self.state = self.SHOW_BALANCE
            self.setText(self.balance)

    def showAmount(self):
        if self.state == self.SHOW_BALANCE:
            self.state = self.SHOW_AMOUNT
            self.setText(self.amount)

class MiniWindow(QtGui.QDialog):
    def __init__(self, actuator, app):
        super(MiniWindow, self).__init__()

        self.clock = Clock()
        self.app = app
        self.actuator = actuator

        self.coinBalance = None
        self.currencies = ['EUR', 'GBP', 'USD']

        self.setMinimumWidth(400)
        self.createComponents()
        self.createLayouts()
        self.createMenu()

        self.show()

    def createComponents(self):
        self.balanceLabel = BalanceLabel(self.changeCurrency)
        self.balanceLabel.setObjectName('balance label')

        self.addressInput = QtGui.QLineEdit()
        self.addressInput.setPlaceholderText('Coin address or contact')
        self.addressInput.setObjectName('address input')
        self.addressInput.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.addressInput.textChanged.connect(self.addressFieldChanged)

        self.addressCompletions = QtGui.QStringListModel()
        addressCompleter = QtGui.QCompleter(self.addressInput)
        addressCompleter.setCaseSensitivity(False)
        addressCompleter.setModel(self.addressCompletions)
        self.addressInput.setCompleter(addressCompleter)

        self.amountInput = QtGui.QLineEdit()
        self.amountInput.setPlaceholderText('... amount')
        self.amountInput.setObjectName('amount input')
        self.amountInput.setFocusPolicy(QtCore.Qt.ClickFocus)

        self.amountValidator = QtGui.QDoubleValidator(self.amountInput)
        self.amountValidator.setNotation(QtGui.QDoubleValidator.StandardNotation)
        self.amountValidator.setDecimals(4)
        self.amountInput.setValidator(self.amountValidator)
        self.amountInput.textChanged.connect(self.amountInputChanged)

        self.sendButton = QtGui.QPushButton('Send')
        self.sendButton.setObjectName('send button')
        self.sendButton.setDisabled(False)
        self.sendButton.clicked.connect(self.send)

        self.createButton = QtGui.QPushButton('Create')
        self.createButton.setObjectName('create button')
        self.createButton.setDisabled(False)
        self.createButton.clicked.connect(self.createGui)

        path = os.path.join(os.getcwd(), 'icons', 'switch.png')
        self.changeButton = QtGui.QPushButton(QtGui.QIcon(path), '')
        self.changeButton.setFlat(False)
        self.changeButton.clicked.connect(self.changeGui)

        self.receivingBox = QtGui.QGroupBox('Select address')
        self.hideAddresses = QtGui.QCheckBox('hide addresses')
        self.hideAddresses.setChecked(False)

    def createLayouts(self):
        self.mainLayout = QtGui.QGridLayout(self)
        self.mainLayout.addWidget(self.balanceLabel, 0, 0)
        self.mainLayout.addWidget(self.changeButton, 0, 3)
        self.mainLayout.addWidget(self.addressInput, 1, 0)
        self.mainLayout.addWidget(self.amountInput, 2, 0)
        self.mainLayout.addWidget(self.sendButton, 2, 1, 1, 1)
        self.mainLayout.addWidget(self.createButton, 2, 2, 1, 2)

        extraLayout = QtGui.QGridLayout()
        extraLayout.addWidget(QtGui.QLabel('--!--'), 0, 0)
        extraLayout.addWidget(self.hideAddresses, 2, 0)
        extraLayout.setColumnMinimumWidth(0, 50)
        self.receivingBox.setLayout(extraLayout)
        self.mainLayout.addWidget(self.receivingBox, 0, 4, -1, 3)

    def createMenu(self):
        self.menuBar = QtGui.QMenuBar()
        menu = self.menuBar.addMenu('Coins')

        quitOption = menu.addAction('Close')
        quitOption.triggered.connect(self.close)

        viewMenu = self.menuBar.addMenu('View')
        walletMenu = self.menuBar.addMenu('Extra')
        viewMenu.addSeparator()

        showReceiving = viewMenu.addAction('Show receiving address')
        showReceiving.setCheckable(True)
        #showReceiving.toggled.connect(self.toggleReceivingLayout)

        helpMenu = self.menuBar.addMenu('Help')
        websiteAction = helpMenu.addAction('Website')
        #websiteAction.triggered.connect(self.launchWebSite())
        helpMenu.addSeparator()
        reportBugAction = helpMenu.addAction('Report Bug')
        #reportBugAction.triggered.connect(self.showReportBug())
        helpMenu.addSeparator()
        aboutAction = helpMenu.addAction('About')
        #aboutAction.triggered.connect(self.aboutAction)
        self.mainLayout.setMenuBar(self.menuBar)

        path = os.path.join(os.getcwd(), 'icons', 'coin.png')
        self.setWindowIcon(QtGui.QIcon(path))
        self.setWindowTitle('coin')
        self.setWindowFlags(QtCore.Qt.Window)
        self.layout().setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.setObjectName('main window')

    def addressFieldChanged(self, address):
        self.addressInput.setText(address)
        #if self.isValid(address):
        #self.check_button_status()
        self.addressInput.setProperty('isValid', True)
        #self.recomputeStyle(self.addressInput)
        #else:
        #self.sendButton.setDisabled(True)
        #self.addressInput.setProperty('isValid', False)
        #self.recomputeStyle(self.addressInput)

        if len(address):
            self.addressInput.setProperty('isValid', None)
            #self.recomputeStyle(self.addressInput)

    def amountInputChanged(self, amount):
        #self.check_buttons_status()
        quote = None
        if quote:
            self.balanceLabel.setAmount(quote)
            self.balanceLabel.showAmount()
        else:
            self.balanceLabel.showBalance()

    def changeCurrency(self, forward=True):
        if forward:
            self.currencies = self.currencies[1:] + self.currencies[0:1]
        else:
            self.currencies = self.currencies[-1:] + self.currencies[0:-1]
        self.resfreshBalance()

    def resfreshBalance(self):
        if self.coinBalance is None:
            return
        self.setBalance()
        self.amountInputChanged(self.amountInput.text())

    def send(self):
        self.actuator.wallet.makeTransaction()

        self.actuator.send(self.addressInput.text(), self.amountInput.text(), self)
        self.addressInput.setText('')
        self.amountInput.setText('')

    def changeGui(self):
        self.hide()
        self.coinGui = CoinGui(self.actuator.wallet, self.app)
        self.coinGui.main()

    def createGui(self):
        print('changeGui')

class MiniActuator:
    def __init__(self, wallet):

        self.wallet = wallet
        self.themeName = 'Sahara'
        self.themes = self.loadThemePaths()

    def selectTheme(self, themeName):
        if themeName in self.themes.keys():
            self.themeName = themeName

    def changeTheme(self, themeName):
        if themeName in self.themes.keys():
            self.themeName = themeName
        self.loadTheme()

    def themeNames(self):
        sorted(self.themes.keys())

    def loadTheme(self):
        try:
            themePrefix, themePath = self.themes[self.themeName]
        except KeyError:
            print('key not found')
            return
        QtCore.QDir.setCurrent(os.path.join(themePrefix, themePath))
        with open('style.css') as styleFile:
            QtGui.qApp.setStyleSheet(styleFile.read())

    def loadThemePaths(self):
        themePaths = {}
        for prefix in [self.localDataDir()]:
            themePaths.update(self.themeDirsFromPrefix(prefix))
        return themePaths

    def loadThemeName(self, themeFullPath):
        try:
            with open(os.path.join(themeFullPath, 'name.cfg')) as nameConfigFile:
                return nameConfigFile.read().rstrip("\n").strip()
        except IOError:
            return None

    def themeDirsFromPrefix(self, prefix):
        if not os.listdir(prefix):
            return []
        themePaths = {}
        for theme in os.listdir(prefix):
            fullPath = os.path.join(prefix, theme)
            themeCss = os.path.join(fullPath, 'style.css')
            if not os.path.exists(themeCss):
                continue
            themeName = self.loadThemeName(fullPath)
            if themeName is None:
                continue
            themePaths[themeName] = prefix, theme
        return themePaths

    def localDataDir(self):
        assert sys.argv
        path = os.path.join(os.getcwd(), 'data')
        return path

    def send(self, address, amount, window):
        if self.wallet.transactionComplete:
            self.waitingDialog(lambda: False if self.wallet.transactionComplete else
                'Sending transaction waiting...')

        message = 'tempMessage'
        TransactionWindow(message, self)

    def waitingDialog(self, method):
        timer = Timer()
        timer.start()
        dialog = QtGui.QDialog()
        dialog.resize(200, 50)
        dialog.setWindowTitle('Coin')
        label = QtGui.QLabel('Sending transaction')
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(label)
        dialog.setLayout(vbox)
        dialog.show()

        def ff():
            print '!!'
            timerState = method()
            if timerState:
                label.setText(timerState)
            else:
                dialog.close()

        dialog.connect(timer, QtCore.SIGNAL('timersignal'), ff)
        dialog.exec_()
        #dialog.destroy()

class CoinLiteGui(QtCore.QObject):
    def __init__(self, wallet, coinWindow=None):
        super(CoinLiteGui, self).__init__()

        self.wallet = wallet
        self.coinWindow = coinWindow

        if self.coinWindow is not None:
            self.app = self.coinWindow.app
        else:
            self.app = QtGui.QApplication(sys.argv)

    def main(self):
        actuator = MiniActuator(self.wallet)
        self.miniWindow = MiniWindow(actuator, self.app)
        actuator.loadTheme()