import random

class Dice:
    """"Introducing variable damage"""



    def __init__(self, sides: int = 6) -> None:
        """"Defining the dice"""

        if sides < 2:
            raise ValueError("The dice must have at least two sides")

        self.sides = sides


    def roll(self):
        """"Getting a random side from the dice"""
        return random.randint(1, self.sides)

    def __repr__(self):
        return f"Dice(sides = {self.sides})"
    

    def __call__(self):

        return self.roll()
        