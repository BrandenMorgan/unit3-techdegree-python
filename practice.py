import re
import random


with open('phrases.txt') as phrases:
    data = phrases.read()
    phrase_list = re.findall(r"[\w?' ]+", data)
random_phrase = random.choice(phrase_list)

phrase = list(random_phrase)
phrase_list = random_phrase.split()

# Add underscores to display before first guess
unguessed_phrase_list = []
for word in phrase_list:
    underscores = len(word) * ['_']
    new_word = ' '.join(underscores)
    unguessed_phrase_list.append(new_word)
unguessed_phrase = ('  ').join(unguessed_phrase_list)
print("\n", unguessed_phrase, '\n')

guess_phrase = []
for x in phrase:
    if x == ' ':
        guess_phrase.append('')
    else:
        guess_phrase.append('_')

def get_guess():
    while True:
        try:
            guess = input('\n' + 'Guess a letter: ')
            if guess == 'EXIT':
                return guess
            if type(guess) != str or len(guess) != 1 or guess in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                raise ValueError
            return guess
        except ValueError:
            print("Your guess must be 1 letter.")


def check_guess(guess, phrase, guess_phrase):
    for c in phrase:
        if c == guess:
            guess_phrase[phrase.index(c)] = c
            phrase[phrase.index(c)] = '*'
    return guess_phrase


already_guessed = []
lives = 5
while '_' in guess_phrase and lives > 0:
    guess = get_guess()
    if guess.upper() == 'EXIT':
        break
    if guess in already_guessed:
        print('\n"{}" was already guessed. Try again.'.format(guess))
    if guess not in phrase and guess not in already_guessed:
        lives -= 1
        print('\nYou have {} lives remaining'.format(lives))
    if guess not in already_guessed:
        already_guessed.append(guess)
    print('\n' + (' ').join(check_guess(guess, phrase, guess_phrase)))

    if '_' not in guess_phrase and lives > 0:
        print('\n' + '#' * 5, "!!!!Congratulations you guessed the phrase!!!!", '#' * 5 + '\n')
    elif '_' in guess_phrase and lives == 0:
        print('\n' + '+ ' * 10, "<<<<<GAME OVER>>>>>", ' +' * 10)
