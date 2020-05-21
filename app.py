# Import your Game class
import random
import re

from phrasehunter.game import Game, phrase_list


# Create your Dunder Main statement.
if __name__ == '__main__':
# Inside Dunder Main:
    
## Create an instance of your Game class
    game = Game(phrase_list)
## Start your game by calling the instance method that starts the game loop
    game.start_game()
# Do I need anything else in here?
