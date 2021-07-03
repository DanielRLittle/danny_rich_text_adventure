class Monster:
    """description should always be a Description object"""
    def __init__(self, description):
        self.alive = True
        self.description = description
        return

    def get_description(self):
        return self.description.get_description(self.alive)

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

       