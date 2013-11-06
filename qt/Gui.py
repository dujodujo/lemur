import sys, os, math, re, hashlib
from Constants import*
from Wallet import*
from AmountEdit import*
from Console import*
from GuiLite import*
from ConfigurationDialog import*

class EnterButton(QtGui.QPushButton):
    def __init__(self, text, funktion):
        super(EnterButton, self).__init__(text)

        self.funktion = funktion
        self.clicked.connect(funktion)

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == QtCore.Qt.Key_Return:
            apply(self.funktion, ())

class HelpButton(QtGui.QPushButton):
    def __init__(self, text):
        super(HelpButton, self).__init__('?')
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setFixedWidth(20)
        self.clicked.connect(lambda : QtGui.QMessageBox.information(self, 'help', text, 'OK'))

class TreeWidget(QtGui.QTreeWidget):
    def __init__(self, parent=None):
        super(TreeWidget, self).__init__(parent)

class StatusStarButton(QtGui.QPushButton):
    def __init__(self, icon, tooltip, func):
        super(StatusStarButton, self).__init__(icon, '')

        self.setToolTip(tooltip)
        self.setFlat(True)
        self.setMaximumWidth(25)
        self.clicked.connect(func)
        self.func = func

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == QtCore.Qt.Key_Return:
            apply(self.func,())

class CoinWindow(QtGui.QMainWindow):
    def __init__(self, wallet):
        super(CoinWindow, self).__init__()

        self.wallet = wallet
        self.app = None

        self.icon = QtGui.QIcon(os.path.join(os.getcwd(),'icons','coin.png'))
        self.tray = QtGui.QSystemTrayIcon(self.icon, self)
        self.tray.setToolTip('Electrum')
        self.tray.activated.connect(self.trayActivated)

        self.buildMenu()
        self.tray.show()
        self.buildTabs()
        self.buildMenuBar()

    def buildTabs(self):
        self.columnsWidth = {
            'contacts' : [200, 100, 300],
            'history' : [100, 100, 100, 100, 100]
        }

        self.tabs = QtGui.QTabWidget(self)
        self.tabs.addTab(self.createHistoryTab(),  'History')
        self.tabs.addTab(self.createSendTab(),     'Send')
        self.tabs.addTab(self.createReceiveTab(),  'Receive')
        self.tabs.addTab(self.createContactsTab(), 'Contacts')
        self.tabs.addTab(self.createConsoleTab(),  'Console')
        self.tabs.setMinimumSize(600,400)
        self.tabs.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self.setCentralWidget(self.tabs)

    def trayActivated(self, reason):
        if reason == QtGui.QSystemTrayIcon.DoubleClick:
            self.showNormal()

    def buildMenu(self, hidden=False):
        menu = QtGui.QMenu()
        if self.isMinimized():
            menu.addAction('Show', self.showNormal)
        else:
            menu.addAction('Hide', self.showMinimized)
        menu.addSeparator()
        menu.addAction('Exit', self.close)
        self.tray.setContextMenu(menu)

        self.buildStatusBar()

    def buildStatusBar(self):
        self.statusBar = QtGui.QStatusBar()
        self.statusBar.setFixedHeight(35)

        self.balanceLabel = QtGui.QLabel('Current balance: ')
        self.statusBar.addWidget(self.balanceLabel)

        accounts = self.wallet.accounts
        if len(accounts) >= 1:
            accountComboBox = QtGui.QComboBox()
            items = ["all accounts"] + accounts.values()
            accountComboBox.addItems(items)
            accountComboBox.setCurrentIndex(0)
            self.connect(accountComboBox, QtCore.SIGNAL('activated(QString)'),
                self.changeAccount)
            self.statusBar.addPermanentWidget(accountComboBox)

        self.loadStatusBarButtons()
        self.setStatusBar(self.statusBar)

    def loadStatusBarButtons(self):
        if self.wallet.WalletLocked:
            lockIcon = QtGui.QIcon(os.path.join(os.getcwd(), 'icons', 'lock.png'))
        else:
            lockIcon = QtGui.QIcon(os.path.join(os.getcwd(), 'icons', 'unlock.png'))

        self.configurationButton = StatusStarButton(QtGui.QIcon(os.path.join(os.getcwd(),
            'icons', 'unconfirmed.png')), 'configuration', self.loadConfiguration)
        self.statusBar.addPermanentWidget(self.configurationButton)

        self.guiLiteButton = StatusStarButton(QtGui.QIcon(os.path.join(os.getcwd(),
            'icons', 'switch.png')), 'guiLite', self.changeGui)
        self.statusBar.addPermanentWidget(self.guiLiteButton)

        self.passwordButton = StatusStarButton(lockIcon, 'Password', lambda: self.changePasswordDialog(self))
        self.statusBar.addPermanentWidget(self.passwordButton)

        self.statusButton = StatusStarButton(QtGui.QIcon(os.path.join(os.getcwd(),
            'icons','status_disconnected.png')), 'Network', self.runNetworkDialog)
        self.statusBar.addPermanentWidget(self.statusButton)

    def changePasswordDialog(self, parent=None):
        dialog = QtGui.QDialog(parent)
        dialog.setModal(True)

        password = QtGui.QLineEdit()
        password.setEchoMode(QtGui.QLineEdit.Password)

        newPassword = QtGui.QLineEdit()
        newPassword.setEchoMode(QtGui.QLineEdit.Password)

        configurePassword = QtGui.QLineEdit()
        configurePassword.setEchoMode(QtGui.QLineEdit.Password)

        vbox = QtGui.QVBoxLayout()
        msg = 'Enter password'
        vbox.addWidget(QtGui.QLabel(msg))

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        #todo
        if False:
            grid.addWidget(QtGui.QLabel('Password'), 1, 0)
            grid.addWidget(password, 1, 1)

        grid.addWidget(QtGui.QLabel('New Password'), 2, 0)
        grid.addWidget(newPassword, 2, 1)

        grid.addWidget(QtGui.QLabel('Confirm password'), 3, 0)
        grid.addWidget(configurePassword, 3, 1)

        vbox.addLayout(grid)
        layout = self.createLayoutOkNo(dialog)
        vbox.addLayout(layout)
        dialog.setLayout(vbox)

        if not dialog.exec_():
            return

    def settingsDialog(self):
        dialog = QtGui.QDialog(self)
        dialog.setWindowTitle('Settings')
        dialog.setModal(True)

        components = self.createSettingsComponents()
        self.createSettingsTabs()
        self.createSettingsGrid(components)
        self.createSettingsLayout(dialog)

        if not dialog.exec_(): return

    def createSettingsComponents(self):
        zeroLabel = QtGui.QLabel('Display zeros:')
        amountEdit = AmountEdit(None)
        amountEdit.setText('%d' % self.wallet.numZeros)

        languages = ['SL', 'EN', 'GER', 'JPN']
        languages.insert(0, 'None')
        languageLabel = QtGui.QLabel('Language:')
        languageCombo = QtGui.QComboBox()
        languageCombo.addItems(languages)
        languageCombo.setCurrentIndex(0)

        currencies = ['EUR', 'GBP', 'USD']
        currencies.insert(0, 'None')
        currencyLabel = QtGui.QLabel('Currency:')
        currencyCombo = QtGui.QComboBox()
        currencyCombo.addItems(currencies)
        currencyCombo.setCurrentIndex(0)

        feeLabel = QtGui.QLabel('Transaction fee')
        feeEdit = AmountEdit(None)
        feeEdit.setText('fee')

        changeBox = QtGui.QCheckBox('Change address')
        changeBox.setChecked(True)

        components = [zeroLabel, amountEdit, languageLabel, languageCombo,
            currencyLabel, currencyCombo, feeLabel, feeEdit, changeBox]
        return components

    def createSettingsTabs(self):
        self.settingsTab = QtGui.QTabWidget(self)
        self.tab1 = QtGui.QWidget()
        self.settingsTab.addTab(self.tab1, 'Display')
        self.tab2 = QtGui.QWidget()
        self.settingsTab.addTab(self.tab2, 'Wallet')

    def createSettingsGrid(self, componets):
        zeroLabel, amountEdit, languageLabel, languageCombo, currencyLabel,\
        currencyCombo, feeLabel, feeEdit, changeBox = componets

        gridUI = QtGui.QGridLayout(self.tab1)
        gridUI.setColumnStretch(0, 1)

        gridUI.addWidget(zeroLabel, 0, 0)
        gridUI.addWidget(amountEdit, 0, 1)
        msg = 'number of zeros after decimal point'
        gridUI.addWidget(HelpButton(msg), 0, 2)

        gridUI.addWidget(languageLabel, 1, 0)
        gridUI.addWidget(languageCombo, 1, 1)
        msg = 'Select language in GUI'
        gridUI.addWidget(HelpButton(msg), 1, 2)

        gridUI.addWidget(currencyLabel, 2, 0)
        gridUI.addWidget(currencyCombo, 2, 1)
        msg = 'Select currency is used'
        gridUI.addWidget(HelpButton(msg), 2, 2)

        gridWallet = QtGui.QGridLayout(self.tab2)
        gridWallet.setColumnStretch(0,1)

        gridWallet.addWidget(feeLabel, 0, 0)
        gridWallet.addWidget(feeEdit, 0, 1)
        msg = 'Transaction fee'
        gridWallet.addWidget(HelpButton(msg), 0, 2)

        gridWallet.addWidget(changeBox, 1, 0)
        msg = 'Change addresses'
        gridWallet.addWidget(HelpButton(msg), 1, 1)

    def createSettingsLayout(self, dialog):
        vboxLayout = QtGui.QVBoxLayout()
        vboxLayout.addWidget(self.settingsTab)
        vboxLayout.addLayout(self.createLayoutOkNo(dialog))
        dialog.setLayout(vboxLayout)

    def createLayoutOkNo(self, dialog):
        buttonLayout = QtGui.QHBoxLayout()
        buttonLayout.addStretch(1)

        okButton = QtGui.QPushButton('Ok')
        buttonLayout.addWidget(okButton)
        okButton.clicked.connect(dialog.accept)

        noButton = QtGui.QPushButton('No')
        buttonLayout.addWidget(noButton)
        noButton.clicked.connect(dialog.reject)

        return buttonLayout

    def changeAccount(self, account):
        if account == 'all accounts':
            self.currentAccount = None
        else:
            accounts = self.wallet.accounts
            for key, value in accounts.items():
                if key == account:
                    self.currentAccount = account

        self.updateHistoryTab()
        self.updateStatus()
        self.updateReceiveTab()

    def runNetworkDialog(self):
        print('run network dialog')

    def createHistoryTab(self):
        self.history = TreeWidget(self)
        self.history.setColumnCount(4)
        for i, width in enumerate(self.columnsWidth['history']):
            self.history.setColumnWidth(i, width)
        self.history.setHeaderLabels(['data', 'description', 'amount', 'balance'])

        self.connect(self.history, QtCore.SIGNAL('itemDoubleClicked(QTreeWidgetItem*, int)'),
            self.historyLabelClicked)
        self.connect(self.history, QtCore.SIGNAL('itemChanged(QTreeWidgetItem*, int)'),
            self.historyLabelChanged)
        self.history.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.history.customContextMenuRequested.connect(self.createHistoryMenu)
        return self.history

    def createSendTab(self):
        widget = QtGui.QWidget()
        components  = self.createSendTabComponents()
        gridlayout = self.createSendTabLayouts(components)
        widget.setLayout(gridlayout)

        widget2 = QtGui.QWidget()
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(widget)
        vbox.addStretch(1)
        widget2.setLayout(vbox)
        return widget2

    def createSendTabComponents(self):
        completer = QtGui.QCompleter()
        completer.setCaseSensitivity(False)

        self.paymentReceiver = paymentReceiver = QtGui.QLineEdit()
        paymentReceiver.setCompleter(completer)
        self.message = message = QtGui.QLineEdit()
        self.amountEdit = amountEdit = AmountEdit(None)
        self.feeEdit = feeEdit = AmountEdit(None)
        sendButton = EnterButton('Send', self.send)
        clearButton = EnterButton('Clear', self.doClear)

        components = [paymentReceiver, message, amountEdit, feeEdit, sendButton, clearButton]
        return components

    def createSendTabLayouts(self, components):
        paymentReceiver, message, amountEdit, feeEdit, sendButton, clearButton = components

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.setColumnMinimumWidth(5, 200)
        grid.setColumnStretch(10,10)

        grid.addWidget(QtGui.QLabel('Payment recipient'), 1, 0)
        grid.addWidget(paymentReceiver, 1, 1, 1, 1)
        grid.addWidget(HelpButton('Recipient of transfer'), 1, 2)

        grid.addWidget(QtGui.QLabel('Description'), 2, 0)
        grid.addWidget(message, 2, 1, 1, 1)
        grid.addWidget(HelpButton('Description of transfer'), 2, 2)

        grid.addWidget(QtGui.QLabel('Amount'), 3, 0)
        grid.addWidget(amountEdit, 3, 1, 1, 1)
        grid.addWidget(HelpButton('Amount sent'), 3, 2)

        grid.addWidget(QtGui.QLabel('Fee'), 4, 0)
        grid.addWidget(feeEdit, 4, 1, 1, 1)
        grid.addWidget(HelpButton('Amount sent'), 4, 2)

        grid.addWidget(sendButton, 6, 1)
        grid.addWidget(clearButton, 6, 2)
        return grid

    def createReceiveTab(self):
        treeWidget, widget, hboxLayout = self.createListTab(['Address', 'Label', 'Balance', 'Transaction'])
        treeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        treeWidget.customContextMenuRequested.connect(self.createReceiveMenu)

        self.connect(treeWidget, QtCore.SIGNAL('itemDoubleClicked(QTreeWidgetItem*, int)'),
            lambda item, column: self.addressLabelClicked(item, column, treeWidget,
                columnAddress=0, columnLabel=1))
        self.connect(treeWidget, QtCore.SIGNAL('itemChanged(QTreeWidgetItem*, int)'),
            lambda item, column: self.addressLabelClicked(item, column, treeWidget,
                columnAddress=0, columnLabel=1))
        self.connect(treeWidget, QtCore.SIGNAL('currentItemChanged(QTreeWidgetItem*, QTreeWidgetItem*)'),
            lambda item, b: self.currentItemChanged(item))

        self.receiveList = treeWidget
        self.receiveButtonsBox = hboxLayout
        hboxLayout.addStretch(1)
        return widget

    def createContactsTab(self):
        treeWidget, widget, hboxLayout = self.createListTab(['Adress', 'Label', 'Tx'])
        treeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        treeWidget.customContextMenuRequested.connect(self.createContactMenu)

        for i, width in enumerate(self.columnsWidth['contacts']):
            treeWidget.setColumnWidth(i, width)

        self.connect(treeWidget, QtCore.SIGNAL('itemDoubleClicked(QTreeWidgetItem*, int)'),
            lambda a,b: self.addressLabelClicked(a,b,treeWidget, 0, 1))
        self.connect(treeWidget, QtCore.SIGNAL('itemChanged(QTreeWidgetItem*, int)'),
            lambda a,b: self.addressLabelChanged(a,b,treeWidget, 0, 1))

        self.contactList = treeWidget
        self.contactsButtonsLayout = hboxLayout
        hboxLayout.addStretch(1)
        return widget

    def createConsoleTab(self):
        self.console = Console()
        self.console.updateNamespace({'wallet' : self.wallet, 'gui' : self})
        return self.console

    def createListTab(self, headers):
        treeWidget = TreeWidget(self)
        treeWidget.setColumnCount(len(headers))
        treeWidget.setHeaderLabels(headers)

        widget = QtGui.QWidget()
        button = QtGui.QWidget()

        vboxLayout = QtGui.QVBoxLayout()
        vboxLayout.setMargin(0)
        vboxLayout.setSpacing(0)

        hboxLayout = QtGui.QHBoxLayout()
        hboxLayout.setMargin(0)
        hboxLayout.setSpacing(0)
        button.setLayout(hboxLayout)

        vboxLayout.addWidget(treeWidget)
        vboxLayout.addWidget(button)

        widget.setLayout(vboxLayout)
        return treeWidget, widget, hboxLayout

    def createContactMenu(self, position):
        item = self.contactList.itemAt(position)
        print('item')
        if not item:
            return
        print('item yes')
        address = unicode(item.text(0))
        label = unicode(item.text(1))
        toAddress = item.data(0,32).toString()
        menu = QtGui.QMenu()
        #menu.addAction('code', lambda: self.showCode('coin: '+address, 'address'))
        #menu.addAction()
        #menu.addAction()

        #self.runHook('Create contact menu', menu, item)
        #menu.exec_(self.contactList.viewport().mapToGlobal(position))

    def createReceiveMenu(self, position):
        print('aaaa')
        #item = self.receiveList.itemAt(position)

    def buildMenuBar(self):
        menuBar = QtGui.QMenuBar()

        menu = menuBar.addMenu('File')
        openWalletAction = menu.addAction('Open Wallet')
        openWalletAction.triggered.connect(self.selectWalletFile)

        preferenceAction = menu.addAction('Preferences')
        preferenceAction.triggered.connect(self.settingsDialog)
        menu.addSeparator()

        transactionMenu = menu.addMenu('Load transaction')
        transactionFile = transactionMenu.addAction('From File')
        transactionFile.triggered.connect(self.processFromFile)
        menu.addSeparator()

        quitItem = menu.addAction('Close')
        quitItem.triggered.connect(self.close)

        walletMenu = menuBar.addMenu('Wallet')
        walletBackupAction = walletMenu.addAction('CreateAction')
        walletBackupAction.triggered.connect(self.backupWallet)

        self.setMenuBar(menuBar)

    def selectWalletFile(self):
        pass

    def processFromFile(self):
        pass

    def backupWallet(self):
        pass

    def showCode(self, data, title="code"):
        if not data:
            return
        dialog = QtGui.QDialog(self)
        dialog.setModal(1)
        dialog.setWindowTitle(title)
        dialog.setMinimumSize(300,300)
        vboxLayout = QtGui.QVBoxLayout()
        #qrw = QtGui.QRCodeWidget(data)
        qwidget =QtGui.QWidget()
        vboxLayout.addWidget(qwidget, 1)
        vboxLayout.addWidget(QtGui.QLabel(data), 0, QtCore.Qt.AlignHCenter)
        hboxLayout = QtGui.QHBoxLayout()
        hboxLayout.addStretch(1)

        button = QtGui.QPushButton("Save")
        hboxLayout.addWidget(button)
        #button.clicked.connect(printQWidget)

        button = QtGui.QPushButton("Close")
        hboxLayout.addWidget(button)
        #button.clicked.connect(dialog.accept)
        #button.setDefault(True)

        vboxLayout.addLayout(hboxLayout)
        dialog.setLayout(vboxLayout)
        dialog.exec_()

    def addressLabelClicked(self, item, column, treeWidget, columnAddress, columnLabel):
        if column == columnLabel and  item.isSelected():
            address = unicode(item.text(columnAddress))
            label = unicode(item.text(columnLabel))
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable |
                QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsDragEnabled)
            treeWidget.editItem(item, column)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable |
                QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsDragEnabled)

    def addressLabelChanged(self, item, column, treeWidget, columnAddress, columnLabel):
        pass

    def currentItemChanged(self, a):
        pass

    def historyLabelClicked(self, item, column):
        if column==2 and item.isSelected():
            self.isEdit = True
            item.setFlags(QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsSelectable |
                QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsEnabled)
            self.history.editItem(item, column)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsUserCheckable |
                QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsDragEnabled)
            self.isEdit = False

    def historyLabelChanged(self, item):
        if self.isEdit:
            self.isEdit = True
            thash = str(item.data(0, QtCore.Qt.UserRole).toString())
            txt = self.wallet.transactions.get(thash)
            text = unicode(item.text(2))
            self.setLabel(thash, text)
            #if text:
            #    item.setForeground(2, QCore.Qt.QBrush(QCore.QColor.black()))
            #else:
                #text = self.wallet.getDefaultLabel(thash)
                #item.setText(2, text)
                #item.setForeground(2, QCore.Qt.QBrush(QCore.QColor.gray()))
            #self.isEdit = False

    def createHistoryMenu(self, position):
        self.history.selectedIndexes()
        item = self.history.currentItem()
        if not item:
            return
        xhash = str(item.data(0, QtCore.Qt.UserRole).toString())
        if not xhash:
            return
        menu = QtGui.QMenu()
        #menu.addAction('details', lambda: self.txShowDetails(self.wallet.transaction.get(xhash)))
        menu.addAction('description', lambda: self.txLabelClicked(item, 2))
        menu.exec_(self.contactList.viewport().mapToGlobal(position))

    def updateHistoryTab(self):
        pass

    def updateStatus(self):
        print('updateStatus')

    def updateReceiveTab(self):
        pass

    def updateContactsTab(self):
        self.contactList.clear()

    def connectSlots(self, sender):
        #self.connect(sender, QtCore.SIGNAL('timer signal'), self.timerActions)
        print('connectSlots')

    def updateWallet(self):
        self.updateStatus()
        self.updateHistoryTab()
        self.updateReceiveTab()
        self.updateContactsTab()

    def send(self):
        pass

    def doClear(self):
        for e in [self.paymentReceiver, self.message, self.amountEdit, self.feeEdit]:
            e.setText('')
        self.updateStatus()

    def changeGui(self):
        self.hide()
        self.lite = CoinLiteGui(self.wallet, self)
        self.lite.main()

    def loadConfiguration(self):
        self.configuration = ConfigurationDialog(self)

    def close(self):
        QtGui.QMainWindow.close(self)

class CoinGui:
    def __init__(self, wallet, app=None):
        self.wallet = wallet
        if app is None:
            self.app = QtGui.QApplication(sys.argv)

    def main(self):
        coinWindow = CoinWindow(self.wallet)
        coinWindow.app = self.app
        coinWindow.updateWallet()
        coinWindow.show()
        self.app.exec_()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    wallet = Wallet()
    coinGui = CoinGui(wallet)
    coinGui.main()