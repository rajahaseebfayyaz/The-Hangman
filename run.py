import random
from words import word_list, stages, welcome_msg, goodbye_msg, rules

# The idea of this game and bit of idea about code has been taken from youtube tutorials and from emmalawlor hangman game  # noqa


class WaterTank:
    """
    Creates an instance of the WaterTank game
    Initializes all attributes required for gameplay
    Displays the WaterTank to the user
    Runs the game by asking the user for input
    Evaluates user input
    Determines result & checks if user wants to play again
    """
    def welcome(self):
        """
        Display welcome message to user
        """
        print(welcome_msg)

    def rules(self):
        """
        Print rules of game
        """
        print(rules)

    def need_rules(self):
        """
        Asks user if they want rules by entering Y or N
        """
        play = input('Do you need rules? (Y/N').strip().upper()  # noqa
        print('\n')
        if play == 'Y':
            self.rules()
        elif play == 'N':
            return
        else:
            print('Invalid choice \n')
            self.need_rules()

    def __init__(self):
        self.word = random.choice(word_list)
        self.stage = 0
        self.guessed_letters = []
        self.guessed_words = []
        # Solution for displaying the hidden word taken from this tutorial https://www.youtube.com/c/KiteHQ  # noqa
        # With underscores replaced by dashes
        self.progress = '-' * len(self.word)
        self.games_played = 0
        self.games_won = 0

    def display_tank_level(self):
        """
        Displays the Water tank image relevant to the amount of lives remaining
        Dsiplays the random word with letters represented by dashes
        """
        print(stages[self.stage])
        print('\n')
        print(self.progress)
        print('\n')

    def display_sorry(self):
        print('Sorry,try again')
        print('\n')

    def display_guesses(self, guess):
        print(f'the letters you have guessed are: ')

        # printing the guesses
        for i in self.guessed_letters:
            print(i, ' ')
        print('\n')

    def play_water_tank(self):
        """
        While user has lost less than 5 lives,
        requests a letter from user & validates input to ensure it is a letter
        checks if the letter is in the word and if it has been guessed already.
        Gives user appropriate feedback.
        Breaks loop when user has correctly guessed all letters
        """
        while self.stage < 5:
            self.display_tank_level()
            guess = input('Choose a letter: ').lower().strip()  # noqa
            print('\n')
            if guess.isalpha() and len(guess) == 1:
                if guess not in self.word:
                    if guess in self.guessed_letters:
                        self.display_sorry()
                    else:
                        self.stage += 1
                        self.guessed_letters.append(guess)
                        self.display_sorry()
                elif guess.isalpha() and guess in self.word:
                    if guess in self.guessed_letters:
                        self.display_sorry()
                    else:
                        print(f'{guess} is in the word!') # noqa
                        print('\n')
                        self.guessed_letters.append(guess)
                        # code for replacing dashes with letters adapted from  # noqa
                        # https://github.com/kiteco/python-youtube-code/blob/master/build-hangman-in-python/hangman.py
                        word_as_list = list(self.progress)
                        indices = [i for i, letter in enumerate(self.word) if letter == guess]  # noqa
                        for index in indices:
                            word_as_list[index] = guess
                            self.progress = "".join(word_as_list)
                        if "-" not in self.progress:
                            print(f'Congrats! You correctly guessed the answer: {self.word}') # noqa
                            print('\n')
                            self.games_won += 1
                            break

            elif guess.isalpha() and guess == self.word:
                print(f'Congrats! You correctly guessed the answer: {self.word}') # noqa
                print('\n')
                self.games_won += 1
                break

            elif guess.isalpha() and guess not in self.word and guess in self.guessed_words:  # noqa
                print(f'You already guessed {guess}, try again')
                print('\n')

            elif guess.isalpha() and guess not in self.word and guess not in self.guessed_words:  # noqa
                print(f'{guess} is not the word, try again') # noqa
                print('\n')
                self.stage += 1
                self.guessed_words.append(guess)
                print('\n')
            else:
                print('Invalid input \n')
        if self.stage >= 6:
            print(stages[self.stage])
            print('\n')
            print(f'Game Over! The word was {self.word}') # noqa
            print('\n')
        self.play_again()

    def play_again(self):
        """
        Asks user if they want to play again by entering Y or N
        Calls display_hangman function while user wants to play again
        """
        play = input(f'Would you like to play again? (Y/N)').strip().upper()  # noqa
        print('\n')
        if play == 'Y':
            self.stage = 0
            self.guessed_letters = []
            self.guessed_words = []
            self.word = random.choice(word_list)
            self.progress = '-' * len(self.word)
            self.games_played += 1
            self.play_water_tank()
        elif play == 'N':
            self.games_played += 1
            print('Thanks for playing! \n')
            print(goodbye_msg)
            print(f'You won {self.games_won} out of {self.games_played} games')
        else:
            print('Invalid choice \n')
            self.play_again()


def main():
    """
    Run water tank game functions
    """
    game = WaterTank()
    game.welcome()
    game.need_rules()
    game.play_water_tank()


print("Lets play WaterTank!")
main()