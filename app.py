import re

from phrasehunter.game import Game


if __name__ == '__main__':
    with open('phrases.txt') as phrases:
        data = phrases.read()
        phrase_list = re.findall(r"[\w?' ]+", data)

    game = Game(phrase_list)
    game.start_game()
