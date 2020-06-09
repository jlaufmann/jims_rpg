"""

Jim's RPG

The hero must challenge and beat opponents until she has accumulated enough points (to reach level 10.

The hero and all opponents have ratings for strength, intelligence and speed.
Strength is on a scale 0-6. If strength drops to 0 the Hero dies.

Intelligence and speed have a range 1-6.

At the start of the game the Hero may use three rolls of the dice to decide intelligence.
Speed is decided from 1 roll of the dice.
Strength starts the game at 4.

Every time the Hero loses(wins) a fight, she loses(gains)  one point of strength, with a max of 6.

When the hero encounters an opponent she can:
r - run away
if the opponent is faster than the hero, the hero is caught and loses strength. The opponent loses speed.
The hero then has the option to attack, talk to, or try again to run away from the opponent.

a - attack
attacking means fighting. The result of the fight is determined by who has the greater score. Score is calculated by
multiplying strength by the dice value.

t - talk
when talking, both the opponent and Hero have the chance to improve.
If talking is successful the intelligence of the opponent increases and the strength of the Hero increases.
The higher the intelligence of the opponent, the greater the chance of success by talking.
If talking doesn't work, the Hero loses strength and the Opponent loses intelligence. The hero then has the option to
attack or to run away.

Hero: 6                             requires 2 or higher
Hero: 5     Opponent: 4 or higher   requires 2 or higher
Hero: 5     Opponent: 3 or lower    requires 3 or higher
Hero: 4     Opponent: 4 or higher   requires 3 or higher
Hero: 4     Opponent: 3 or lower    requires 4 or higher
Hero: 3     Opponent: 4 or higher   requires 4 or higher
Hero: 3     Opponent: 3 or lower    requires 5 or higher
Hero: 2     Opponent: 4 or higher   requires 5 or higher
Hero: 2     Opponent: 3 or lower    requires 6
Hero: 1                             requires 6

Before deciding on an action, the Hero can see the strength and intelligence of the opponent, but not the speed.
For each challenge the speed of the Hero may change slightly, it can be +/-1, randomly determined at challenge time.

To be able to challenge the next opponent, the Hero must have been able to run away, successfully talk to the opponent
or have fought the opponent.

The hero must run out of opponents or pass 5 opponents to win the game.

There is a large pool of opponents and for each challenge a random opponent is drawn from the pool.

If the hero beats an opponent in a fight, the opponent is removed from the pool.
If the hero has run away from an opponent the opponent remains in the pool with decreased strength and speed.
If the hero has successfully talked to the opponent, the opponent remains in the pool however with increased
intelligence and decreased strength.


"""

from jrpgdefs import *

###############
achilles = Opponent('Achilles', 3, 3, 6)
aphrodite = Opponent('Aphrodite', 4, 5, 3)
apollo = Opponent('Apollo', 5, 4, 3)
asteria = Opponent('Asteria', 4, 4, 2)
artemis = Opponent('Artemis', 5, 4, 3)
athena = Opponent('Athena', 3, 5, 4)
atlas = Opponent('Atlas', 6, 1, 1)
chaos = Opponent('Chaos', 2, 1, 3)
eros = Opponent('Eros', 4, 6, 4)
hades = Opponent('Hades', 4, 2, 3)
nemesis = Opponent('Nemesis', 5, 5, 4)
perseus = Opponent('Perseus', 2, 3, 5)
phoebe = Opponent('Phoebe', 3, 3, 3)
poseidon = Opponent('Poseidon', 4, 4, 3)
prometheus = Opponent('Prometheus', 4, 4, 3)
rhea = Opponent('Rhea', 2, 3, 6)
zeus = Opponent('Zeus', 6, 5, 3)

opponents = [achilles, aphrodite, apollo, asteria, artemis, athena, atlas, chaos, eros, hades, nemesis, perseus,
             phoebe, poseidon, prometheus, rhea, zeus]

player = Hero()
player.name = input(f"What is your name? ")

deaths = 0  # when the hero has 5 deaths or runs out of opponents, they win. Maybe.
kills = []

tryagain = 'y'
count = 0
print(f"Welcome to the game {player.name}!")
print(f"Your intelligence level will be decided with a maximum of three dice rolls.")
while tryagain != 'n' and count < 3:
    player.intelligence = random.randint(1, 6)
    count += 1
    print(f"Attempt {count}/3: {player.intelligence}")
    if count < 3:
        tryagain = input(f"Try again? (y/n): ").lower()

print(f"Your intelligence is {player.intelligence}.")

player.strength = random.randint(1, 6)
player.speed = random.randint(1, 6)
print(f"Decided by a roll of the dice, your strength is {player.strength} and your speed is {player.speed}.")

while player.strength > 0:

    print(f"\nChallenges faced: {player.challenges}")

    if player.status != 'engaged2':
        print(f"Dead opponents: {kills}")
        print(f"Potential opponents: ", end='')
        for god in opponents:
            print(god, end=', ')  # not quite perfect, there's a comma at the end of the line!!!
        print('')

    if player.status == 'free':
        print("\nYou can do the following:\n"
              "w - walk around\n"
              "c - check condition\n"
              "q - quit")
        player.todo()
        if player.action == 'q':
            quit()
        elif player.action == 'c':
            player.print()
        else:
            player.status = random.choice(['free', 'engaged'])

    if player.status == 'engaged':
        opponent = random.choice(opponents)
        print(f"\n{opponent.name} has seen you.")

    # engaged2 happens when running away or talking fails
    if player.status == 'engaged' or player.status == 'engaged2':
        opponent.print()
        player.print()
        player.youcan()
        player.todo()

    if player.action == 'a':
        if player.attack(opponent) == 'won':
            print(f"\nYou defeated {opponent.name}. He/She is now dead. Congratulations!")
            kills.append(opponent.name)
            opponents.remove(opponent)
            if not player.strengthen():  # this could be removed if strength shouldn't increase after a fight
                player.fasten()
        else:
            print(f"\nYour attack against {opponent.name} failed!")
            player.weaken()
            opponent.strengthen()
        player.challenges += 1
        player.status = 'free'

    if player.action == 'r':
        if player.race(opponent) == 'escaped':
            print(f"\nCongratulations you coward, you ran away from {opponent.name}.")
            opponent.slowen()
            opponent.weaken()
            if opponent.strength == 0:
                print(f"{opponent.name} now has {opponent.strength}. He/she is dead.")
                kills.append(opponent.name)
                opponents.remove(opponent)
            player.status = 'free'
        else:
            print(f"\nSlowpoke. {opponent.name} caught you. You have lost strength (and respect).")
            player.weaken()
            opponent.fasten()
            player.status = 'engaged2'
        player.challenges += 1

    if player.action == 't':
        if player.discuss(opponent) == 'success':
            print(f"\nCongratulations, your diplomatic tactics paid off!")
            if not player.strengthen():
                player.fasten()
            opponent.smarten()
            opponent.weaken()
            if opponent.strength == 0:
                print(f"{opponent.name} is now dead.")
                kills.append(opponent.name)
                opponents.remove(opponent)
            player.status = 'free'
        else:
            print(f"\nYou failed as a diplomat.")
            player.weaken()
            opponent.dumben()
            player.status = 'engaged2'
        player.challenges += 1

    if len(opponents) == 0:
        print(f"Congratulations!! Everybody is dead.")
        print(f"You won facing {player.challenges} challenges resulting in {len(kills)} deaths.")
        break

if player.strength == 0:
    print(f"You have {player.strength} strength. You are dead.")
    print(f"You faced {player.challenges} challenges resulting in {len(kills)} other deaths.")
    print(f"The dead are: {kills}")
    print(f"Still roaming free are: ", end='')
    for god in opponents:
        print(god, end=', ')  # not quite perfect, there's a comma at the end of the line!!!
    print('')
    print(f"Game Over.")
