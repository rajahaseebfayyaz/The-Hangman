import random
from words import word_list

def get_word():
  word = random.choice(word_list)
  return word.upper()

  def play(word):
      word_completion = "_" * len(word)
      guessed = False
      guessed_letters = []
      guessed_words = []
      tries = 6
      print("Let's play Hangman!")
      print(display_hangman(tries))
      print(word_completion)
      print("/n") 
      while not guessed and tries > 0:
          guess = input("Please guess a letter or word: ").upper()
          if len(guess) == 1 and guess.isalpha():
              if guess in guessed_letters:
                  print("You already guessed the letter" , guess)
                  elif guess not in word:
                      print(guess ,"is not in the word.")
                      tries -= 1
                      guessed_letters.append guess
                      else:
                          print("Good job,", guess, "is i the word!")
                          guessed_letters.append(guess)
                          word_as_list = list(word_completion)

                      elif len(guess) == len(word) and guess.isalpha():

                  else:
                      print("Not a valid guess.")
                      print(display_hangman(tries))
                      print(word_completion)
                      print("/n")

                      
 
