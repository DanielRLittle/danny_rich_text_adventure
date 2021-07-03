from player import Player
from level import Level, Dungeon
from scene import Scene
from monster import Monster
from description import Description

levels = []

# It's time to game
def main():
    danny = Player()
    create_world()
    active_level = levels[0]
    active_level.open()

    monsta = Monster(Description(
        "The monsta lies on the floor, seemingly lifeless as you stare into its bloodshot eyes that were so recently set on your demise. It might make a nice stew!",
        "The bloodthirsty monsta stares at you, its bloodshot eyes burning with hatred. You get the impression it might be eyeing you up for a nice stew..."))

    print(monsta.get_description())

    print("You attack!")
    monsta.die()

    print(monsta.get_description())

def create_world():
    dungeon = Dungeon()
    dungeon.set_scenes([Scene("An empty room."), Scene("A pot of gold."), 
              Scene("A goblin."), Scene("A fancy goblin.")])
    levels.append(dungeon)

if __name__ == "__main__":
    main()
