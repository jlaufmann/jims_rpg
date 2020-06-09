"""

Jim's RPG

As of 09.06.2020 this readme file was just extracted from the jrpgmain.py file

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