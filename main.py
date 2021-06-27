from player import Player
from level import Level, Dungeon
from scene import Scene

levels = []

# It's time to game
def main():
    danny = Player()
    create_world()
    active_level = levels[0]
    active_level.open()

def create_world():
    dungeon = Dungeon()
    dungeon.set_scenes([Scene("An empty room."), Scene("A pot of gold."), 
              Scene("A goblin."), Scene("A fancy goblin.")])
    levels.append(dungeon)

if __name__ == "__main__":
    main()
