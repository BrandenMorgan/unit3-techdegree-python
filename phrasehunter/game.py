import random
import time

from .phrase import Phrase


class Game:
    def __init__(self, phrases):
        self.phrases = [Phrase(item) for item in phrases]
        self.current_phrase = random.choice(self.phrases)
        self.lives = 5

    def unguessed_phrase(self):
        unguessed_phrase = []
        for x in self.current_phrase.character_list:
            if x == ' ':
                unguessed_phrase.append(' ')
            else:
                unguessed_phrase.append('_')
        return (' ').join(unguessed_phrase)

    def get_guess(self):
        while True:
            try:
                guess = input('\n' + 'Guess a letter: ')
                if guess == 'EXIT':
                    return guess
                if not guess.isalpha() or len(guess) != 1:
                    raise ValueError
                return guess
            except ValueError:
                print("Your guess must be 1 letter.")

    def make_guess(self, guess):
        self.current_phrase.guess(guess)
        return self.current_phrase.show_phrase()

    def start_game(self):
        phrase = self.current_phrase.character_list
        already_guessed = []
        show_guess = self.unguessed_phrase()
        print("\nType 'EXIT' to exit.")
        print('\n' + show_guess)
        self.make_guess(' ')
        while '_' in show_guess and self.lives > 0:
            guess = self.get_guess()
            if guess.upper() == self.current_phrase.character_list[0]:
                show_guess = self.make_guess(guess.upper())
            if guess == self.current_phrase.character_list[0]:
                show_guess = self.make_guess(guess.lower())
            show_guess = self.make_guess(guess)
            if guess.upper() == 'EXIT':
                time.sleep(.5)
                print('\n...Goodbye\n')
                time.sleep(.5)
                break
            if guess in already_guessed:
                print('\n"{}" was already guessed. Try again.'.format(guess))
            if guess not in phrase and guess not in already_guessed:
                self.lives -= 1
                print('\nYou have {} out of 5 lives remaining!'.format(self.lives))
            if guess not in already_guessed:
                already_guessed.append(guess)
            print('\n' + (' ').join(show_guess))

            if '_' not in show_guess and self.lives > 0:
                print('\n' + '#' * 5, "!!!!Congratulations you guessed the phrase!!!!", '#' * 5 + '\n')
                play_again = input("Would you like to play again? [y]es/[n]o: ")
                if play_again.upper() in ['Y', 'YES']:
                    self.lives = 5
                    self.current_phrase = random.choice(self.phrases)
                    phrase = self.current_phrase.character_list
                    already_guessed = []
                    show_guess = self.unguessed_phrase()
                    print('\n' + show_guess)
                    self.make_guess(' ')
                    continue
                print("\n***** Thank you for playing *****")
                time.sleep(.5)
                print('\n...Goodbye\n')
                time.sleep(.5)
                break

            elif '_' in show_guess and self.lives == 0:
                print('\n' + '+ ' * 10, "<<<<<GAME OVER>>>>>", ' +' * 10 + '\n')
                play_again = input("Would you like to play again? [y]es/[n]o: ")
                if play_again.upper() in ['Y', 'YES']:
                    self.lives = 5
                    self.current_phrase = random.choice(self.phrases)
                    phrase = self.current_phrase.character_list
                    already_guessed = []
                    show_guess = self.unguessed_phrase()
                    print('\n' + show_guess)
                    self.make_guess(' ')
                    continue
                print("\n***** Thank you for playing *****")
                time.sleep(.5)
                print('\n...Goodbye\n')
                time.sleep(.5)
                break
