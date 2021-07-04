class Monster:
    """description should always be a Description object"""
    def __init__(self, description, hostility):
        self.alive = True
        self.description = description
        self.default_hostility = True
        self.hostility = hostility

    def get_description(self):
        return self.description.get_description(self.alive)

    def is_hostile(self, other):
        if type(other) not in self.hostility:
            self.hostility[type(other)] = self.default_hostility
        return self.hostility[type(other)]

    def attack(self):
        return

    def drop_loot(self):
        return

    def taunt(self):
        return

    def calculateXP(self):
        return

    def move(self):
        return

    def die(self):
        self.alive = False
