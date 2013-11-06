import math
import random

from System import*
from Scene import*
from Systems.EquipmentSystem.EquipmentButtons import*

class TestSystem(Scene):
    items_loaded = False

    def __init__(self, engine):
        Scene.__init__(self)

        self.engine = engine
        self.db = self.engine.db

        print("TestSystem")
