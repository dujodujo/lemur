from Entities.Hero import Hero

class Commands(object):
    def __init__(self):
        pass

    def execute(self, entity): pass
    def reset(self, entity): pass

class Attack(Commands):
    def __init__(self):
        Commands.__init__(self)

    def execute(self, entity):
        print('execute attack')
        entity.set_animation(entity.command_sprites[2])

    def reset(self, entity):
        print('reset attack')
        entity.set_animation(entity.command_sprites[1])
        entity.animation.finished = False

class Defend(Commands):
    def __init__(self):
        Commands.__init__(self)

    def execute(self, entity):
        print('execute defend')
        entity.set_animation(entity.command_sprites[3])

    def reset(self, entity):
        print('reset defend')
        entity.set_animation(entity.command_sprites[1])
        entity.animation.finished = False

class Heal(Commands):
    def __init__(self):
        Commands.__init__(self)

    def execute(self, entity):
        print('execute heal')
        entity.set_animation(entity.command_sprites[4])

    def reset(self, entity):
        print('reset heal')
        entity.set_animation(entity.command_sprites[1])
        entity.animation.finished = False