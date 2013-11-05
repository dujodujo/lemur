import random
class Die():
    def __int__(self):
        self.roll()
        print(self.getValue())

    def roll(self):
        self.value = random.randint(1,6)
        return self.value

    def getValue(self):
        return self.value

class Dice(list):
    def __init__(self, diceList=None):
        super(list, self).__init__(diceList)
        
    def rollDice(self):
        [Die.roll(d) for d in self]

    def getTotal(self):
        return sum(self)

    def getTuple(self):
        return tuple([Die.getValue(d) for d in self])

    def matching(self):
        self.rollDice()
        return self[0].getValue() == self[1].getValue()