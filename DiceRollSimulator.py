import random

class DiceRollSimulator:
    def roll_the_dice(self):
        return random.randint(1,6)
    
dice_roll_sim = DiceRollSimulator()
score = dice_roll_sim.roll_the_dice()
print(f"{score}")  