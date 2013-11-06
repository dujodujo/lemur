scenes = ["MainMenu", "CreateHeroSystem", "CreateEnemySystem",
          "BattleSystem", "BattleMenu", "SplashSystem",
          "EquipmentSystem", "TestSystem", "InventorySystem"]

def create(engine, name):
    scene = __import__('Systems.' + name + '.' + name, globals(), locals(), [name], -1)
    return getattr(scene, name)(engine = engine)