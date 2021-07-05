from random import choice

class Monster:
    """description should always be a Description object"""
    def __init__(self, description, taunts = []):
        self.alive = True
        self.description = description
        self.taunts = taunts
        return

    def get_description(self):
        return self.description.get_description(self.alive)

    def attack(self):
        return

    def drop_loot(self):
        return

    def taunt(self):
        """Picks a taunt from the taunts list and prints it."""
        try:
            taunt_picked = choice(self.taunts)
            print(f"The monster smiles, and says: {taunt_picked}")
        except IndexError:
            # if no taunts in list, print nothing
            return 
        

    def calculateXP(self):
        return

    def move(self):
        return

    def die(self):
        self.alive = False

       