import random

class Cards(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.faces = {1:"A", 10:"T", 11:"J", 12:"Q", 13:"K"}

    def __str__(self):
        if self.rank in self.faces:
            return "{}{}".format(self.faces[self.rank],self.suit)
        else:
            return "{}{}".format(self.rank,self.suit)

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __ne__(self, other):
        return self.rank != other.rank or self.suit != self.suit

    def __lt__(self, other):
        if self.rank < other.rank:
            return True
        else:
            return False

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

class Deck(object):
    def __init__(self):
        self.cards = []
        for rank in range(1,14):
            for suit in "CDHS":
                card = Cards(rank,suit)
                self.cards.append(card)

    def __iter__(self):
        return self

    def deal(self):
        random.shuffle(self.cards)
        return random.choice(self.cards)

