#from enum import Enum 
import enum

# this is a level
class LevelTypes(enum.Enum):
    DUNGEON = 0

class Level():
    def __init__(self, type, complete=False):
        self.type = type

    def open(self):
        """Opens the level."""
        print(f"Welcome to this {self.type.name.lower()}")
        # if self.type == LevelTypes.DUNGEON:

class Dungeon(Level):
    def __init__(self):
        super().__init__(LevelTypes.DUNGEON)

    def open(self):
        super().open()
        print("The walls are very shiny from all the blood on them.\n" 
              "Clearly, your enemy has been here before you.")
        active_level = True