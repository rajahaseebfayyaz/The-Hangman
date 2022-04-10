# Water Tank

## Author 
Raja Haseeb Fayyaz

## Project Overview 


Water Tank is a simple hangman type game. You can test yourself against rules section and you can play as many times as you want and when you are done you'll know how many games you have won, while keeping track of your score. There's even a rules section, so if you've never played before now is the perfect oppertunity!  

### Flow Chart 

## Design Documents

- In the early planning stages, a flowchart was drawn up to help visualise the steps required to create a functioning water tank game. 
- This chart was helpful to the developer when creating functions as the logic of the game was broken down into simple steps.
- [This flowchart](https://1drv.ms/b/s!AtrJulJDGsm2qFf5wKQGuJDN1MRH) was created using [Lucidchart](https://www.lucidchart.com/pages/landing?utm_source=google&utm_medium=cpc&utm_campaign=_chart_en_tier1_mixed_search_brand_exact_&km_CPC_CampaignId=1490375427&km_CPC_AdGroupID=55688909257&km_CPC_Keyword=lucidcharts&km_CPC_MatchType=e&km_CPC_ExtensionID=&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=442433236001&km_CPC_TargetID=aud-826163889020:kwd-84176206937&km_CPC_Country=20483&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&mkwid=sMDuh5elr_pcrid_442433236001_pkw_lucidcharts_pmt_e_pdv_c_slid__pgrid_55688909257_ptaid_aud-826163889020:kwd-84176206937_&gclid=Cj0KCQjw1ouKBhC5ARIsAHXNMI-XHJRavE5VCyXoRZMUJrufGkLIFrq_iz1oKO4xAXMed81uEqSRagMaAsA5EALw_wcB)
![image](https://user-images.githubusercontent.com/84344402/133690510-8f1d770e-ccfe-4bea-908d-a1321736cb1d.png)


## How To Play

- The game is filled with Over 5000 words.
- The computer will then pick a random choice.
- The user has the option of viewing the rules, which tells them how to play.
- The screen than tells user of how many guesses he/she have remaining.
- User chooses the alphabet to complete the guess word
- if the alphabet is in the word the game automatically moves forward to next guess word and if not than user loses one lifeline
- sorry try again message displays on top
- Once user loses all lifelines and water tank fills with man drowning user will be given choice to play again or leave
- if user chooses not to play further than user will be greeted with goodbye message also updating of the score  

## Features 

### Implemented Features 

#### Welcome Message:

<img width="516" alt="image" src="https://user-images.githubusercontent.com/87448281/162604989-14f732b4-163a-4313-bbd4-f9ad7cd0ce73.png">


WELCOME TO


 _      ____  _____  _____ ____    _____  ____  _      _  __
/ \  /|/  _ \/__ __\/  __//  __\  /__ __\/  _ \/ \  /|/ |/ /
| |  ||| / \|  / \  |  \  |  \/|    / \  | / \|| |\ |||   / 
| |/\||| |-||  | |  |  /_ |    /    | |  | |-||| | \|||   \ 
\_/  \|\_/ \|  \_/  \____\\_/\_\    \_/  \_/ \|\_/  \|\_|\_\
                                                            


A game like hangman brought to you by Raja

#### Rules Question:

<img width="539" alt="image" src="https://user-images.githubusercontent.com/87448281/162605003-9bc0fb9d-2c64-4688-8a50-fb92a1b2a8fc.png">


 ______    __   __  ___      _______  _______ 
|    _ |  |  | |  ||   |    |       ||       |
|   | ||  |  | |  ||   |    |    ___||  _____|
|   |_||_ |  |_|  ||   |    |   |___ | |_____ 
|    __  ||       ||   |___ |    ___||_____  |
|   |  | ||       ||       ||   |___  _____| |
|___|  |_||_______||_______||_______||_______|

Water tank is easy and fun to play.

Guess the word before the tank fills and you win.

You can guess an entire word or a letter at at time, but play wisely,
you only have 5 stages before you run out of air.

Repeating guesses you already made will not count against your tries.

#### Play Game:

- When start playing gives user choice of 5 guesses
- Each time user guesses correct alphabet game continues
- When guessed wrong alphabets after 5 tries the game is over thus displaying the user scores

#### Made user input easier by:

- Case insensitivity can enter W and w etc. 
- Leading/trailing space stripping.
- Users don't have to type entire letters for Yes No validation, but keeping it simple.

#### Recap Guessed letters and Guessed words:

-gives insights of guessed letters and words of which user selects

#### Death by Drowning stages represented with pixelated images:
stages =
       
       
       # initial Guy is on dry land
       """
       --------------------
       |                  |
       |      O           |
       |     \\|/          |
       |      |           |
       |     / \\          |
       --------------------""",

       # guy is knee deep in water
       """
       --------------------
       |                  |
       |      O           |
       |     \\|/          |
       |      |           |
       --------------------
       --------------------""",
      
       # guy is waste deep in water
       """
       --------------------
       |                  |
       |      O           |
       |     \\|/          |
       --------------------
       --------------------
       --------------------""",

       # guy is shoulder deep in water
       """
       --------------------
       |                  |
       |      O           |
       --------------------
       --------------------
       --------------------
       --------------------""",
       
      # guy is covered in water, BUT THERE IS AIR AT THE TOP
       """
       --------------------
       |                  |
       --------*-----------
       --------------------
       --------------------
       --------------------
       --------------------
       --------------------""",

       # final Stage: totally underwater, NO AIR
        """
         -------------------- 
         --------------------
         --------------------
         --------------------
         --------------------
         --------------------
         --------------------
         --------------------""",
 

#### Play again and Goodbye message:

- Score tracker
- Allows users to see how many games they have won vs the computer.

### Future Features 
#### Google sheets to collect usernames and show 'Most Addicted Players'
- This feature would collect usernames and compare them to a google doc, user's could then view what user has played the most. 
- This feature would also show their wins and losses. 
- Due to time restriction this could not be added to this version. 

## Model / Class
### Parameters 
def __init__(self):
        -self.word = random.choice(word_list)
        -self.stage = 0
        -self.guessed_letters = []
        -self.guessed_words = []
        # Solution for displaying the hidden word taken from this youttube
        # With underscores replaced by dashes
        -self.progress = '-' * len(self.word)
        -self.games_played = 0
        -self.games_won = 0

### Methods: 
copy def functions with self and explanations docstring

 def __init__(self):
        self.word = random.choice(word_list)
        self.stage = 0
        self.guessed_letters = []
        self.guessed_words = []
        # Solution for displaying the hidden word taken from this youttube
        # With underscores replaced by dashes
        self.progress = '-' * len(self.word)
        self.games_played = 0
        self.games_won = 0
        
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
            
             def display_tank_level(self):
        """
        Displays the Water tank image relevant to the amount of lives remaining
        Dsiplays the random word with letters represented by dashes
        """
        self.display_guesses()
        print(stages[self.stage])
        print('\n')
        print(self.progress)
        print('\n')
        
        def display_sorry(self):
        print('Sorry,try again')
        print('\n')
        
        def display_guesses(self):
        """
        Recap the guesses player has made and number
        of tries left to solve the puzzle
        """
        # join from https://stackoverflow.com/questions/12309976/how-do-i-convert-a-list-into-a-string-with-spaces-in-python  # noqa
        print(f"GUESSES REMAINING: {5 - self.stage}")
        if len(self.guessed_letters) > 0:
            print(" GUESSED LETTERS:")
            print(f"   {' '.join(self.guessed_letters)}")
        if len(self.guessed_words) > 0:
            print(" GUESSED WORDS:")
            print(f"   {' '.join(self.guessed_words)}")
        print('\n')
        
        def play_water_tank(self):
        """
        While user has lost less than 5 lives,
        requests a letter from user & validates input to ensure it is a letter
        checks if the letter is in the word and if it has been guessed already.
        Gives user appropriate feedback.
        Breaks loop when user has correctly guessed all letters
        """
        # loop through stages/tries
        while self.stage < 5:
            self.display_tank_level()
            guess = input('Choose a letter: ').lower().strip()  # noqa
            print('\n')
            # check that input is a single letter
            if guess.isalpha() and len(guess) == 1:
                # check if guess is a part of the word
                if guess not in self.word:
                    # # check if guess is not in letter
                    if guess in self.guessed_letters:
                        self.display_sorry()
                         # check if guessed letter is not a part of word
                    else:
                        self.stage += 1
                        self.guessed_letters.append(guess)
                        self.display_sorry()
                        
                elif guess.isalpha() and guess in self.word:
                    # comment here for next line of code
                    if guess in self.guessed_letters:
                        self.display_sorry()
                        # comment here for next line of code
                    else:
                        print(f'{guess} is in the word!')
                        print('\n')
                        self.guessed_letters.append(guess)
                        # code for replacing dashes with letters adapted from  # noqa
                        # https://github.com/kiteco/python-youtube-code/blob/master/build-hangman-in-python/hangman.py
                        word_as_list = list(self.progress)
                        indices = [i for i, letter in enumerate(self.word) if letter == guess]  # noqa
                        # comment here for what loop does
                        for index in indices:
                            word_as_list[index] = guess
                            self.progress = "".join(word_as_list)
                            # comment here for next line of code
                        if "-" not in self.progress:
                            print(f'Congrats! You correctly guessed the answer: {self.word}')  # noqa
                            print('\n')
                            self.games_won += 1
                            break

            elif guess.isalpha() and guess == self.word:
                print(f'Congrats! You correctly guessed the answer: {self.word}')  # noqa
                print('\n')
                self.games_won += 1
                break

            elif guess.isalpha() and guess not in self.word and guess in self.guessed_words:  # noqa
                print(f'You already guessed {guess}, try again')
                print('\n')

            elif guess.isalpha() and guess not in self.word and guess not in self.guessed_words:  # noqa
                print(f'{guess} is not the word, try again')
                print('\n')
                self.stage += 1
                self.guessed_words.append(guess)
                print('\n')
            else:
                print('Invalid input \n')
        if self.stage >= 5:
            print(stages[self.stage])
            print('\n')
            print(f'Game Over! The word was {self.word}')
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

## Testing

- if user entered the word it doesn't count twice
- if user makes wrong choice it doesn't count 

### Validator Testing 
## PEP8 

- When I first put my code through PEP8, i got a few errors. 
<img width="884" alt="image" src="https://user-images.githubusercontent.com/87448281/162600974-d9595529-38aa-4b21-b667-9a66455752c2.png">


- I used ' # noqa' to overried the lines being too long to maintain the readability of the code. I also had to manually fix some whitespace errors. 
<img width="944" alt="image" src="https://user-images.githubusercontent.com/87448281/162600949-79685ad8-711c-4560-bf0a-4ad3ea15874c.png">

## Defects 

I have manually tracked and fixed errors in github and they were mainly indentation errors such as irreregular spacing and irrelevent spaces.

## Deployments 
### Heroku 
The site was deployed to Heroku. The steps to deploy are as follows: 
  - First, you must log into Heroku and go into the settings tab. 
  ![deployment-one]<img width="1437" alt="image" src="https://user-images.githubusercontent.com/87448281/162602097-f68673be-ea63-4a85-acc9-5a4f68fc342b.png">

  - From here, you go to the Config Vars section. 
  ![deployment-two]<img width="1260" alt="image" src="https://user-images.githubusercontent.com/87448281/162602121-d853a669-624e-4d0c-bf54-70cb2cd40e91.png">

  - You then enter Key: PORT and Value: 8000. 
  ![deployment-three]<img width="1386" alt="image" src="https://user-images.githubusercontent.com/87448281/162602161-4eb9741e-1543-4bb2-a4ce-e4e37e400069.png">

  - You must then go to the buildpacks section. Here you add Python and Nodejs. The must be in the order of python on top, and Nodejs underneath. 
  ![deployment-four]<img width="1350" alt="image" src="https://user-images.githubusercontent.com/87448281/162602185-ae0627c0-5245-45e4-b394-3b868f732b3e.png">

  - After finishing the above you will go to the 'Deploy' tab. 
  ![deployment-five]<img width="1401" alt="image" src="https://user-images.githubusercontent.com/87448281/162602211-ffce11d5-9c16-4096-b700-fc2cf725035a.png">

  - You then connect to your Github account. 
  ![deployment-six]<img width="1365" alt="image" src="https://user-images.githubusercontent.com/87448281/162602226-1fe073b8-e50d-499a-921a-32c30190cb73.png">

  - Once you enter your repository name, your Github project will be connected to Heroku. 
  ![deployment-seven]<img width="1325" alt="image" src="https://user-images.githubusercontent.com/87448281/162602237-ed662f75-f394-4e8b-93ce-6eb29d0536b3.png">

  - From here you have two options to deploy. You can select the option to enable automatic deploys, so when you commit any changes will automatically deploy. 
  ![deployment-eight]<img width="1332" alt="image" src="https://user-images.githubusercontent.com/87448281/162602258-54812f06-c4d6-4eb4-ae48-ce25e3a97ee7.png">

  - The second option is to manually deploy, this is what I personally chose. When you click the 'Deploy' button, you will watch your files being uploaded. 
  ![deployment-nine]<img width="1330" alt="image" src="https://user-images.githubusercontent.com/87448281/162602268-8bacf046-ac6a-4c23-9c62-d6ddecba08aa.png">

  -   Once this is complete, a sucess message will appear with a 'View' button that will bring you to the deployed project. 


The live link can be found here - https://thehangman2022.herokuapp.com/
### Credits 

#### Media
- I made the flow chart using the lucidchart.

## Acknowledgments
- My mentor Malia, as always, helped me throught this project. She helped me push this project above and beyond. 
- My original code was inspired from few youtube tutorials and also from emmalawlor project.
- I learned how to use the class in python using this article. [Class atricle](https://www.scraggo.com/python-classes-guess-the-number/)
- [Code Institute Template ](https://github.com/Code-Institute-Org/python-essentials-template)- The Template for the GUI for this project was provided by Code Institute. This allows for the Command line to be shown and used within the browser.
- The fonts for game display taken from this website patorjk.com
