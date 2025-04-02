from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец стреляет из лука."


class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает новое оружие.")

    def attack(self):
        if self.weapon:
            print(self.weapon.attack())
        else:
            print("Боец безоружен и не может атаковать!")


class Monster:
    def __init__(self, name):
        self.name = name

    def defeat(self):
        print(f"Монстр {self.name} побежден!")


fighter = Fighter("Герой")
monster = Monster("Дракон")

sword = Sword()
bow = Bow()

fighter.change_weapon(sword)
fighter.attack()
monster.defeat()

fighter.change_weapon(bow)
fighter.attack()
monster.defeat()

