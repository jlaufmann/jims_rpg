"""
Contains the objects to play the game

"""

import random


def roll():
    return random.randint(1, 6)


class Hero:
    def __init__(self, name='nombre', strength=0, intelligence=0, speed=0, status='free', challenges=0, action='w'):
        self.name = name
        self.strength = strength
        self.intelligence = intelligence
        self.speed = speed
        self.status = status
        self.challenges = challenges
        self.action = action

    def print(self):
        print(f"You ({self.name}) have strength {self.strength}, intelligence {self.intelligence} and "
              f"speed ca. {self.speed}.")

    def todo(self):
        self.action = input("What do you want to do? ").lower()

    def youcan(self):
        print(f"You can:\na - attack\nr - try to run away\nt - talk")

    def attack(self, other):
        if self.strength * roll() >= other.strength * roll():
            return 'won'
        else:
            return 'lost'

    def race(self, other):
        if self.speed + random.randint(-1, 1) >= other.speed + random.randint(-1, 1):
            return 'escaped'
        else:
            return 'caught'

    def discuss(self, other):
        dice = roll()
        # Hero: 6                             requires 2 or higher
        if self.intelligence == 6:
            if dice >= 2: return 'success'
        # Hero: 5     Opponent: 4 or higher   requires 2 or higher
        elif self.intelligence == 5 and other.intelligence >= 4:
            if dice >= 2: return 'success'
        # Hero: 5     Opponent: 3 or lower    requires 3 or higher
        elif self.intelligence == 5:
            if dice >= 3: return 'success'
        # Hero: 4     Opponent: 4 or higher   requires 3 or higher
        elif self.intelligence == 4 and other.intelligence >= 4:
            if dice >= 3: return 'success'
        # Hero: 4     Opponent: 3 or lower    requires 4 or higher
        elif self.intelligence == 4:
            if dice >= 4: return 'success'
        # Hero: 3     Opponent: 4 or higher   requires 4 or higher
        elif self.intelligence == 3 and other.intelligence >= 4:
            if dice >= 4: return 'success'
        # Hero: 3     Opponent: 3 or lower    requires 5 or higher
        elif self.intelligence == 3:
            if dice >= 5: return 'success'
        # Hero: 2     Opponent: 4 or higher   requires 5 or higher
        elif self.intelligence == 2 and other.intelligence >= 4:
            if dice >= 5: return 'success'
        # Hero: 2     Opponent: 3 or lower    requires 6
        elif self.intelligence == 2:
            if dice >= 6: return 'success'
        # Hero: 1                             requires 6
        elif dice >= 6:
            return 'success'
        else:
            return 'failed'

    def strengthen(self):
        if self.strength < 6:
            self.strength += 1
            print(f"You are now stronger!")
            return True
        else:
            return False

    def weaken(self):
        self.strength -= 1
        print(f"You are now weaker!")

    def fasten(self):
        if self.speed < 6:
            self.speed += 1
            print(f"You are now faster!")
            return True
        else:
            return False

    def slowen(self):
        if self.speed > 0:
            self.speed -= 1
            print(f"You are now slower!")
            return True
        else:
            return False

    def smarten(self):
        if self.intelligence < 6:
            self.intelligence += 1
            print(f"You are now smarter!")
            return True
        else:
            return False

    def dumben(self):
        if self.intelligence > 1:
            self.intelligence -= 1
            print(f"You are now dumber!")
            return True
        else:
            return False


class Opponent:
    def __init__(self, name, strength, intelligence, speed):
        self.name = name
        self.strength = strength
        self.intelligence = intelligence
        self.speed = speed

    def __str__(self):
        return f"{self.name}"

    def print(self):
        print(f"{self.name} has strength {self.strength}, intelligence {self.intelligence}, and speed {self.speed}.")

    def strengthen(self):
        if self.strength < 6:
            self.strength += 1
            print(f"{self.name} is now stronger!")
            return True
        else:
            return False

    def weaken(self):
        self.strength -= 1
        print(f"{self.name} is now weaker!")

    def fasten(self):
        if self.speed < 6:
            self.speed += 1
            print(f"{self.name} is now faster!")
            return True
        else:
            return False

    def slowen(self):
        if self.speed > 0:
            self.speed -= 1
            print(f"{self.name} is now slower!")
            return True
        else:
            return False

    def smarten(self):
        if self.intelligence < 6:
            self.intelligence += 1
            print(f"{self.name} is now smarter!")
            return True
        else:
            return False

    def dumben(self):
        if self.intelligence > 1:
            self.intelligence -= 1
            print(f"{self.name} is now dumber!")
            return True
        else:
            return False
