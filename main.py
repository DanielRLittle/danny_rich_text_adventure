from player import Player
from monster import Monster
from description import Description

# It's time to game
def main():
    danny = Player(gender="male")
    print(f"Danny is a {danny.gender} human")

    monsta = Monster(Description(
        "The monsta lies on the floor, seemingly lifeless as you stare into its bloodshot eyes that were so recently set on your demise. It might make a nice stew!",
        "The bloodthirsty monsta stares at you, its bloodshot eyes burning with hatred. You get the impression it might be eyeing you up for a nice stew..."))

    print(monsta.get_description())

    print("You attack!")
    monsta.die()

    print(monsta.get_description())

if __name__ == "__main__":
    main()
