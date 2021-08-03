from random import choice, randint

class Monster:
    """description should always be a Description object"""
    def __init__(self, description, hostility, loot, taunts = []):
        self.alive = True
        self.description = description
        self.default_hostility = True
        self.hostility = hostility
        # The first item of loot must be an int, and sets the max_coins.
        self.max_coins = loot[0]
        self.loot = loot[1:]
        self.taunts = taunts
        return

    def get_description(self):
        return self.description.get_description(self.alive)

    def is_hostile(self, other):
        if type(other) not in self.hostility:
            self.hostility[type(other)] = self.default_hostility
        return self.hostility[type(other)]

    def attack(self):
        return

    def drop_loot(self):
        """Creates a random inventory for this monster with number of coins 
        and random items from list, and prints the result."""
        loot_dropped = []

        coins_dropped = randint(0, self.max_coins)
        if coins_dropped > 1:
            loot_dropped.append(f"{coins_dropped} coins")
        elif coins_dropped == 1:
            loot_dropped.append(f"{coins_dropped} coin")
        
        num_items = randint(0, 3)
        for i in range(0, num_items):
            if self.loot:
                item_picked = choice(self.loot)
                loot_dropped.append(item_picked)
                self.loot.remove(item_picked)

        if loot_dropped:
            print("You find:")
            for item in loot_dropped:
                print(f"- {item}")
        else:
            print("Their pockets are empty; you find nothing of value.")

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
