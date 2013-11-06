from Constants import*
from Clock import*

class Transaction:
    def __init__(self, raw):
        self.testData = {
            'version': '01',
            'inputs': ['a', 'b', 'c', 'd'],
            'outputs': {
                'address': ['a', 'b', 'c', 'd'],
                'value': ['1', '2', '3', '4']
            },
            'lockTime': '0'
        }

    def deserialize(self):
        pass

    def parseTransaction(self, cds):
        d = {
            'version':None,
            'inputs':None,
            'outputs': {
                'address':None,
                'value':None
            },
            'lockTime':None
        }
        return d

class Wallet():
    def __init__(self):
        self.numZeros = 0
        self.accounts = {}
        self.accounts.setdefault('account', {})
        self.labels = {}
        self.labels.setdefault('labels', {})
        self.transactions = {}
        self.transactions.setdefault('transaction', {})
        self.addressbook = {}
        self.addressbook.setdefault('contacts', [])

        self.WalletLocked = False

        if self.accounts.get(0) is None:
            self.accounts['account'] = 'Main account'

        for key, value in self.transactions.items():
            self.transactions[key] = Transaction(value)

    def makeTransaction(self):
        self.transactionComplete = True

    def addContact(self, address, label=None):
        self.addressbook.append(address)
        if label:
            self.labels[address] = label

    def deleteContact(self, address):
        if address in self.addressbook:
            self.addressbook.remove(address)

    def fillAddressbook(self):
        pass

    def getAccounts(self):
        pass

    def getAddressBalance(self, address):
        pass

    def getAccountAddresses(self, address):
        account = self.accounts[address]
        return account

    def getAccountBalance(self, account):
        addressBalance = 0
        if account is None:
            return self.getBalance()
        for address in self.getAccountAddresses(account):
            currentBalance = self.getAddressBalance(address)
            addressBalance += currentBalance
        return addressBalance

    def getBalance(self):
        accountBalance = 0
        for accountKey in self.accounts.keys():
            currentBalance = self.getAccountBalance(accountKey)
            accountBalance += currentBalance
        return accountBalance

    def updatePasswords(self, oldPass, newPass):
        if newPass == '':
            newPass = None

    def save(self):
        data = {
            'accounts' : self.accounts,
            'labels' : self.labels,
            'contacts' : self.addressbook,
            'transactions' : self.transactions
        }

if __name__ == '__main__':
    wallet = Wallet()