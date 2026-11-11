from game_simulator_v1 import Character



class Battle:
    "Managing turn-based combat between two Character objects"

    def __init__(self, hero: Character, enemy: Character):
        """
        Initialise the Character
        """

        self.hero = hero
        self.enemy = enemy

    def play_round(self):
        self.hero.attack(self.enemy)
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)

    def simulated_battle(self):

        round_nr = 1


        while self.hero.is_alive and self.enemy.is_alive:
            self.play_round()
            round_nr += 1

        winner = self.hero if self.hero.is_alive else self.enemy
        print(f" Winner: {winner}")
    
        return winner


    

