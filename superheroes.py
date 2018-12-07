import random
import time
import sys


class Ability:
    ''' ability class '''

    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength

    def attack(self):
        min_attack = self.attack_strength // 2
        max_attack = self.attack_strength
        return random.randint(min_attack, max_attack)

    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength


class Weapon(Ability):
    ''' weapon class '''

    def attack(self):
        print("Using {} to attack".format(self.name))
        return random.randint(0, self.attack_strength)


class Armor:
    ''' armor class '''

    def __init__(self, name, defense):
        self.name = name
        self.defense = defense

    def defend(self):
        return random.randint(0, self.defense)


class Hero:
    ''' hero class '''

    def __init__(self, name, health=100):
        self.abilities = list()
        self.name = name
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def defend(self):
        ''' hero defends self '''
        armor = 0
        for item in self.armors:
            armor += item.defense
        print("hero is defending")
        return armor

    def take_damage(self, damage_amt):
        ''' hero receives damage from enemy '''
        self.health -= damage_amt
        print("{} damage amount:{} ".format(self.name, damage_amt))
        if self.health <= 0:
            print("{} is down".format(self.name))
            self.deaths += 1
            print(self.deaths)
        print("Hero took {} damage".format(damage_amt))

    def add_kill(self, kill):
        ''' modify hero kill count +1 '''
        self.kills += kill
        print("Hero increased Kill Count")

    def attack(self):
        ttldmg = 0
        for ability in self.abilities:
            print("{} was used by {}".format(ability.name, self.name))
            ttldmg += ability.attack()
        print("{} damage was done by {}".format(ttldmg, self.name))
        print("Hero attacked")
        return ttldmg

    def add_ability(self, ability_name, power):
        print("{} ability added".format(ability_name))
        ability = Ability(ability_name, power)
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)


class Team:
    ''' team class made of heroes '''

    def __init__(self, team_name):
        self.name = team_name
        self.heroes = list()

    def add_hero(self, hero):
        self.heroes.append(hero)
        print(" {} added to {}".format(self.heroes[-1].name, self.name))

    def remove_hero(self, name):
        print("attempting to remove hero:", name)
        if self.heroes == []:
            print("Error: there are no heroes in this list")
            return 0
        for hero in self.heroes:
            if hero.name == name:
                print("\nfound hero to remove:", hero.name)
                self.heroes.remove(hero)
            else:
                print("hero not found")
                return 0

    def defend(self, damage):
        print("defending against {}".format(damage))
        dmgpts = damage / len(self.heroes)
        deaths = 0
        for hero in self.heroes:
            hero.health -= (dmgpts - hero.defend())
            if hero.health <= 0:
                deaths += 1
        return deaths

    def attack(self, enemyteam):
        print("attacking {}".format(enemyteam.name))
        if len(enemyteam.heroes) == 0:
            print("There is no one on {}".format(enemyteam.name))
            return 0
        ttldmg = 0
        for hero in self.heroes:
            print(hero.name)
            ttldmg += hero.attack()
        dmgpts = ttldmg / len(enemyteam.heroes)
        dmgpts = 1000
        our_kills = 0
        for hero in enemyteam.heroes:
            hero.take_damage(dmgpts)
            if hero.deaths > 0:
                our_kills += 1
        for hero in self.heroes:
            hero.kills += our_kills
        return ttldmg

    def revive_heroes(self):
        print("Healing {}".format(self.name))
        for hero in self.heroes:
            hero.health = 60

    def find_hero(self, name):
        if self.heroes == []:
            print("there are no heroes in this list")
            return 0
        for hero in self.heroes:
            if hero.name == name:
                print("{} found".format(name))
                return hero
            else:
                print("hero not found")
                return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)


class Arena:

    def __init__(self):
        self.team_one = Team("Red Team")
        self.team_two = Team("Blue Team")
        self.running = True

    def l00p(self):
        while self.running == True:
            self.team_battle()
        else:
            print("Shutting down loop in 3 seconds")
            time.sleep(3)
            sys.exit(0)

    def build_team_one(self):
        hero1 = Hero(input("Name a hero > "))
        hero1.add_ability(input("Name an ability > "),
                          random.randint(1, 5) * 10)
        hero1.add_ability(input("Name another ability > "),
                          random.randint(1, 5) * 10)

        hero2 = Hero(input("Name a hero > "))
        hero2.add_ability(input("Name an ability > "),
                          random.randint(1, 5) * 10)
        hero2.add_ability(input("Name another ability > "),
                          random.randint(1, 5) * 10)

        self.team_one = Team(input("Name this new team > "))
        self.team_one.add_hero(hero1)
        self.team_one.add_hero(hero2)

    def build_team_two(self):
        hero1 = Hero(input("Name a hero > "))
        hero1.add_ability(input("Name an ability > "),
                          random.randint(1, 5) * 10)
        hero1.add_ability(input("Name another ability > "),
                          random.randint(1, 5) * 10)

        hero2 = Hero(input("Name a hero > "))
        hero2.add_ability(input("Name an ability > "),
                          random.randint(1, 5) * 10)
        hero2.add_ability(input("Name another ability > "),
                          random.randint(1, 5) * 10)

        self.team_two = Team(input("Name this new team > "))
        self.team_two.add_hero(hero1)
        self.team_two.add_hero(hero2)

    def team_battle(self):
        self.team_one.attack(self.team_two)
        self.team_two.attack(self.team_one)


if __name__ == "__main__":

    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.l00p()
    time.sleep(5)
    arena.running = False
