class Character:
    def __init__(self, char):
        if type(char) != str or len(char) != 1:
            raise ValueError("Your character must be 1 letter.")
        self.original = char
        self.was_guessed = False

    def __str__(self):
        return self.original

    def exists(self, guess):
        if guess not in self.original:
            return self.was_guessed
        if guess in self.original:
            self.was_guessed = True
        return self.was_guessed

    def show(self):
        if self.was_guessed:
            return self.original
        return '_'
