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
