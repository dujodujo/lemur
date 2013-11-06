from Constants import*
import httplib
import json
import threading
from decimal import Decimal

class Exchanger(threading.Thread):
    def __init__(self, parent):
        threading.Thread.__init__(self)
        self.parent = parent
        self.daemon = True
        self.currencies = None
        self.lock = threading.Lock()
        self.start()

    def exchange(self, coinAmount, currentCurrency):
        with self.lock:
            if self.currencies is None:
                return None
        if currentCurrency not in self.currencies:
            return None
        return coinAmount* self.currencies[currentCurrency]

    def run(self):
        self.discovery()

    def discovery(self):
        try:
            connection = httplib.HTTPConnection('www.google.si')
            connection.request("GET", "/ticker")
        except:
            return
        response = connection.getresponse()
        """
        if response.reason == httplib.responses[httplib.NOT_FOUND]:
            return
        try:
            response = json.loads(response.read())
        except:
            return
        currencies = {}
        try:
            for r in response:
                currencies[r]= self.lookupRate(response, r)
            with self.lock:
                self.currencies = currencies
            self.parent.emit(QtCore.SIGNAL('refreshBalance'))
        except KeyError:
            pass
        """

    def lookupRate(self, response, currencyID):
        pass

    def getCurrencies(self):
        if self.currencies is None:
            return []
        else:
            return sorted(self.currencies.keys())

if __name__ == '__main__':
    exchanger = Exchanger(('EUR', 'USD', 'YEN'))
    exchanger.run()
