from enum import Enum 

# this is a level
class LevelTypes(Enum):
    DUNGEON = 0

class Level():
    def __init__(self, type):
        self.type = type

    def open(self):
        """Opens the level."""
        print(f"Welcome to this {self.type.name.lower()}")

    def set_scenes(self, scenes):
        self.scenes = scenes

    def change_scene(self, scene):
        """Initialises the scene."""
        scene.open()

class Dungeon(Level):
    def __init__(self):
        super().__init__(LevelTypes.DUNGEON)

    def open(self):
        super().open()
        print("The walls are very shiny from all the blood on them.\n" 
              "Clearly, your enemy has been here before you.")
        self.change_scene(self.scenes[0])