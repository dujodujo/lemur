import os
from Constants import*
from collections import defaultdict
from Entity import ChangeListener

class Inventory(ChangeListener):
    max_amount = 100
    def __init__(self, entity_i):
        ChangeListener.__init__(self)

        self.entity_i = entity_i
        self.items = defaultdict()

    def save(self, db):
        for item, amount in self.items.iteritems():
            db('INSERT INTO inventory(rowid, item, amount) VALUES(?, ?, ?)',
                self.entity_i, item, amount)

    def load(self, db):
        inventory = db('SELECT * FROM inventory WHERE rowid=?', self.entity_i)[0]

    def add_item(self, item, amount):
        if item not in self.items and amount < Inventory.max_amount:
            self.items.setdefault(item, amount)
        else:
            self.items[item] = max(Inventory.max_amount, self.items[item]+amount)

    def remove_item(self, item, amount):
        self.items[item] = max(0, self.items[item]-amount)

    def available_items(self):
        return [item for item, amount in self.items.iteritems() if amount > 0]

    def is_item_available(self, item):
        return self.items[item] > 0

    def __len__(self):
        return len(self.available_items())