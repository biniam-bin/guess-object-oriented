import random
from utils.util import GuessingGameTools

Tool = GuessingGameTools()
minimum_number = 0
maximum_number = 100

####### Game Logic ###########

class GuessingGame:
    def __init__(self, player_name = ""):
        self.player_name = player_name


    def get_user_name(self):
        self.player_name = input("YOUR NAME $ ")


    def show_player(self):
        print(f"\t\t\t\tDear {self.player_name} welcome to this game!!")

    def play(self):
        while True:
            secret_number = Tool.generat_random_number(min=minimum_number, max=maximum_number)
            print(secret_number)
            break



####### Game Logic End ###########



Tool.show_title()
Guess = GuessingGame()
Guess.get_user_name()
Guess.show_player()
Tool.show_rules(min=minimum_number, max=maximum_number)
Guess.play()