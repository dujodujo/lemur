import random

class StockBlock(object):
    def __init__(self, purchDate, purchPrice, shares):
        self.date = purchDate
        self.purchPrice = purchPrice
        self.shares = shares

    def __str__(self):
        return "{} {} {}".format(self.date, self.purchPrice, self.shares)

    def getShares(self):
        return self.shares

    def getPurchValue(self):
        return self.purchPrice * self.shares

    def getSaleValue(self, salePrice):
        self.salePrice = salePrice
        return self.salePrice * self.shares

    def getROI(self):
        return (self.salePrice - self.purchPrice) / self.purchPrice

class Position(object):
    def __init__(self, name, symbol, blocks):
        self.name = name
        self.symbol = symbol
        self.myBlocks = blocks
        self.myShares = [StockBlock.getShares(stb) for stb in self.myBlocks]

    def __str__(self):
        return "{:20} {:10} {:<10} {:1}".format(self.name, self.symbol, \
                                               sum(self.myShares), round(self.getROI(),2))

    def getPurchValue(self):
        return sum([StockBlock.getPurchValue(stb) for stb in self.myBlocks])

    def getSalePriceValue(self, salePrice):
        return sum([StockBlock.getSaleValue(stb, salePrice) for stb in self.myBlocks])

    def getROI(self):
        return sum([StockBlock.getROI(stb) for stb in self.myBlocks])

if __name__ == '__main__':

    blocksEK = [
    StockBlock( purchDate='25-Jan-2001', purchPrice=35.86, shares=22 ),
    StockBlock( purchDate='25-Apr-2001', purchPrice=37.66, shares=21 ),
    StockBlock( purchDate='25-Jul-2001', purchPrice=38.57, shares=20 ),
    StockBlock( purchDate='25-Oct-2001', purchPrice=27.61, shares=28 ),]

    blocksGM = [
    StockBlock( purchDate='25-Jan-2001', purchPrice=44.89, shares=17 ),
    StockBlock( purchDate='25-Apr-2001', purchPrice=46.12, shares=17 ),
    StockBlock( purchDate='25-Jul-2001', purchPrice=52.79, shares=15 ),
    StockBlock( purchDate='25-Oct-2001', purchPrice=37.73, shares=21 ),]

    portfolio= [
    Position( "General Motors", "GM", blocksGM ),
    Position( "Eastman Kodak", "EK", blocksEK ),
    Position( "Caterpillar", "CAT",
    [ StockBlock( purchDate='25-Oct-2001',
    purchPrice=42.84, shares=18 )])]


    gm, ek, cat = portfolio[0], portfolio[1], portfolio[2]
    company_shares = (gm, ek, cat)

    gm.getSalePriceValue(salePrice=50)
    cat.getSalePriceValue(salePrice=62)
    ek.getSalePriceValue(salePrice=45)
    
    print("{:20} {:10} {:10} {}".format("Name", "Ticker", "Shares", "ROI"))
    for cs in company_shares:
        print(cs)