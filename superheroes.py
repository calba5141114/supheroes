import random


class Ability(object):

    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        ''' releases a value between 0 and the max attack value'''
        return random.randint(0, self.max_damage)


class Hero(object):

    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = self.starting_health
        self.abilities = []
        self.living = True

    def add_ability(self, ability):
        ''' adds ability to hero abilities '''
        self.abilities.append(ability)

    def attack(self):
        ''' return somes of abilities '''
        for ability in self.abilities:
            return ability.attack()

    def take_damage(self, damage):
        ''' update hero health '''
        self.current_health = self.current_health - damage

    def is_alive(self):
        
        if self.current_health > 0:
            return True
        elif self.current_health <= 0
            return False

    def fight(self, opponent):

        while self.living

        pass
