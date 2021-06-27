class Player():

    def __init__(self, hp=100, gender="neutral", speed=5):
        self.hp = hp
        self.gender = gender

    def get_hp(self):
        return self.hp

    def set_hp(self, new_hp):
        self.hp = new_hp

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender
