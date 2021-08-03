from player import Player
from level import Level, Dungeon
from scene import Scene
from monster import Monster
from description import Description

levels = []
monsta_taunts = ['"Mmm, you look tasty. I could make a nice stew out of you!"',
                '"Hahaha, you are so puny... Shame, not enough meat for a good stew."',
                '"Why did you have to disturb me during my stew-eating? Then again, it did need more seasoning."',
                '"Well, well, well... Look what the cat dragged in... Stew-ingredient number five..."']
monsta_loot = [10, "a spoon still greasy with stew (1c)", 
                "a statue of a golden monkey (100c)", "a family picture (0c)", 
                "a jar filled with a strange substance (quest item)",
                "an empty pouch (0c)"]

# It's time to game
def main():
    danny = Player()
    create_world()
    active_level = levels[0]
    active_level.open()

    monsta = Monster(Description(
        "The monsta lies on the floor, seemingly lifeless as you stare into its bloodshot eyes that were so recently set on your demise. It might make a nice stew!",
        "The bloodthirsty monsta stares at you, its bloodshot eyes burning with hatred. You get the impression it might be eyeing you up for a nice stew..."),
        { type(Player): True, type(Monster): True }, 
        monsta_loot, monsta_taunts)

    print(monsta.get_description())

    monsta_hostility = monsta.is_hostile(danny)
    print(" ".join([f"The monsta is { 'hostile' if monsta_hostility else 'friendly' }.",
        f"You should probably { 'attack' if monsta_hostility else 'sit down for a nice cup of tea' }!"]))
        
    if monsta_hostility:
        print("You attack, but miss!")
        monsta.taunt()
        print("The monster attacks, but misses!")
        print("You attack, and hit! You deal 8 damage!")
        monsta.die()

        print(monsta.get_description())
        print("You search the body for loot.")
        monsta.drop_loot()
    else:
        print("You sit for a nice cup of tea. +1XP")

        print(monsta.get_description())

def create_world():
    dungeon = Dungeon()
    dungeon.set_scenes([Scene("An empty room."), Scene("A pot of gold."), 
              Scene("A goblin."), Scene("A fancy goblin.")])
    levels.append(dungeon)

if __name__ == "__main__":
    main()
