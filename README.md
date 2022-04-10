# Water Tank

## Author 
Raja Haseeb Fayyaz

## Project Overview 


Water Tank is a simple hangman type game. You can test yourself against rules section and you can play as many times as you want and when you are done you'll know how many games you have won, while keeping track of your score. There's even a rules section, so if you've never played before now is the perfect oppertunity!  

### Flow Chart 


## How To Play
- OVER 5000 WORDS
- The computer will then pick a random choice.
- The user has the option of viewing the rules, which tells them how to play.  

## Features 

### Implemented Features 

#### Welcome Message

#### Rules Question

#### Play Game

#### Made user input easier by:
- Case insensitivity can enter W and w etc. 
- Leading/trailing space stripping.
- Users don't have to type entire letters for Yes No validation, but keeping it simple.

#### Recap Guessed letters and Guessed words

#### Dearh by Drowning stages represented with pixelated images

#### PLay again

#### Goodbye message

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

3-4

## Deployments 
### Heroku 
The site was deployed to Heroku. The steps to deploy are as follows: 
  - First, you must log into Heroku and go into the settings tab. 
  ![deployment-one](https://github.com/KateEllen/rock-paper-scissors/blob/main/assets/images/documentation/deployment-one.png)
  - From here, you go to the Config Vars section. 
  ![deployment-two](https://github.com/KateEllen/rock-paper-scissors/blob/main/assets/images/documentation/deployment-two.png)
  - You then enter Key: PORT and Value: 8000. If you have a google sheet installed you will need to enter the data here too. 
  ![deployment-three](https://github.com/KateEllen/rock-paper-scissors/blob/main/assets/images/documentation/deployment-three.png)
  - You must then go to the buildpacks section. Here you add Python and Nodejs. The must be in the order of python on top, and Nodejs underneath. 
  ![deployment-four](https://github.com/KateEllen/rock-paper-scissors/blob/main/assets/images/documentation/deployment-four.png)
  - After finishing the above you will go to the 'Deploy' tab. 
  ![deployment-five](https://github.com/KateEllen/rock-paper-scissors/blob/main/assets/images/documentation/deployment-five.png)
  - You then connect to your Github account. 
  ![deployment-six](https://github.com/KateEllen/rock-paper-scissors/blob/main/assets/images/documentation/deployment-six.png)
  - Once you enter your repository name, your Github project will be connected to Heroku. 
  ![deployment-seven](https://github.com/KateEllen/rock-paper-scissors/blob/main/assets/images/documentation/deployment-seven.png)
  - From here you have two options to deploy. You can select the option to enable automatic deploys, so when you commit any changes will automatically deploy. 
  ![deployment-eight](https://github.com/KateEllen/rock-paper-scissors/blob/main/assets/images/documentation/deployment-eight.png)
  - The second option is to manually deploy, this is what I personally chose. When you click the 'Deploy' button, you will watch your files being uploaded. 
  ![deployment-nine](https://github.com/KateEllen/rock-paper-scissors/blob/main/assets/images/documentation/deployment-nine.png)
  -   Once this is complete, a sucess message will appear with a 'View' button that will bring you to the deployed project. 

  ### Local/Gitpod
  - Click Gitpod button or add it if you don't have it to chrome. 
  - Once Gitpod is open, type ```pip3 install -r requirements.txt``` in the terminal. 
  ![deployment-one-local](https://github.com/KateEllen/rock-paper-scissors/blob/main/assets/images/documentation/gitpod-one.png)
  - Then type ```python3 run.py``` in the terminal. This will start the game. 
  ![deployment-two-local](https://github.com/KateEllen/rock-paper-scissors/blob/main/assets/images/documentation/gitpod-two.png)

The live link can be found here - https://thehangman2022.herokuapp.com/
### Credits 

#### Media
- I made the flow chart using this. [Flow Chart](https://app.diagrams.net/)

## Acknowledgments
- My mentor Malia, as always, helped me throught this project. She helped me push this project above and beyond. 
- My original code was inspired from this video. [Youtube Video](https://www.youtube.com/watch?v=-JACmC8kabo)
- I learned how to use the class in python using this article. [Class atricle](https://www.scraggo.com/python-classes-guess-the-number/)
- [Code Institute Template ](https://github.com/Code-Institute-Org/python-essentials-template)- The Template for the GUI for this project was provided by Code Institute. This allows for the Command line to be shown and used within the browser.
- The colorama website helped to show me how to use it correctly [colorama](https://pypi.org/project/colorama/)
