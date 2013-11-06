from Constants import*
from System import ButtonObject
from System import Texture
from System import WindowObject
from Scene import*

from collections import defaultdict

class InventorySystem(Scene):
    items_loaded = False

    def __init__(self, engine):
        Scene.__init__(self)

        self.engine = engine
        self.engine.all_items = {}
        self.engine.all_equipments = {}

        if not InventorySystem.items_loaded:
            self.save_items()
            InventorySystem.items_loaded = True

    def save_items(self):
        for root, dirs, files in os.walk(Paths.ITEM_PATH):
            if root.endswith('equipment'):
                equipments = {equipment.split('.png')[0]: os.path.join(root, equipment)
                    for equipment in files if equipment.endswith('.png')}
                for key, value in equipments.iteritems():
                    self.engine.db('INSERT INTO equipments(equipment_name, equipment_image) VALUES(?, ?)',
                        key, value)
                self.add_objects(equipments, self.engine.all_equipments)
            elif root.endswith('item'):
                items = {item.split('.png')[0]: os.path.join(root, item)
                    for item in files if item.endswith('.png')}
                for key, value in items.iteritems():
                    self.engine.db('INSERT INTO items(item_name, item_image) VALUES(?, ?)',
                        key, value)
                self.add_objects(items, self.engine.all_items)

    def add_objects(self, inventory_objects, all_objects):
        for obj, path in inventory_objects.iteritems():
            if obj not in all_objects:
                all_objects[obj] = (path, ImageObject(Texture(path)))