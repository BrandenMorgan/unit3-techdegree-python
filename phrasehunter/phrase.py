from .character import Character


class Phrase:
    def __init__(self, phrase):
        self.phrase = []
        self.character_list = list(phrase)

        for letter in phrase:
            self.phrase.append(Character(letter))

    def guess(self, guess):
        for obj in self.phrase:
            obj.exists(guess)

    def show_phrase(self, guess):
        guess_phrase = []
        for obj in self.phrase:
            guess_phrase.append(obj.show())
        return guess_phrase
