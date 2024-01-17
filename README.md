# Battleship Game

The Battleship Game is a little game that is hard to beat and will bring out the most competitive side from the player. The player is competing against the computer in one round of Battleship. It starts with the player entering it's name to get greeted by the computer. Then it's time to guess on a row number and a column number within the board size, or else it will give an error message and ask again. Once valid values are entered, the player will see the guess that was made and then get the results of whether the ship sank or if it was a miss. It will also show what row and column the hidden ship was located on.

### **You can find the project live [here](https://ramona-battleship-game-eb3c0634ab53.herokuapp.com/)**

## UX

The game is made for people that enjoys Battleship games and similar games. The game idea is simple but it's hard to beat the computer which brings out the competative side in the user playing it.

## Goals

The goals are as follows:

- The players want to be able to understand the purpose of the game from the start.
- The players want the game to be easy to understand and follow.
- The players want the game to be a challenge that's not too easy to win.
- The players want to know whether they won or not.
- The players want to know where the hidden ship was located to see if they were close.

## Flow chart

![Flow chart](https://res.cloudinary.com/dpk2gl3yf/image/upload/v1705522208/Start_Game_keuukf.png)

## Game overview

### Loss:

![Game overview](https://res.cloudinary.com/dpk2gl3yf/image/upload/v1705521740/game-view_wcx7at.png)

### Win:

![Game win](https://res.cloudinary.com/dpk2gl3yf/image/upload/v1705528466/winner_c2xalg.png)

### If the player enters invalid values:

**Rows**

![Error: Invalid row value](https://res.cloudinary.com/dpk2gl3yf/image/upload/v1705523840/row-error1_b5kgzg.png)

![Error: Invalid row value](https://res.cloudinary.com/dpk2gl3yf/image/upload/v1705521741/row-error2_oih4uu.png)

**Columns**

![Error: Invalid column value](https://res.cloudinary.com/dpk2gl3yf/image/upload/v1705521740/column-error1_rdawar.png)

![Error: Invalid column value](https://res.cloudinary.com/dpk2gl3yf/image/upload/v1705521740/column-error2_v6gbgu.png)

# Testing

- The game starts correctly as it should without problems.
- The instructions shows from the start which is correct.
- The player gets asked to enter it's name which gets returned as a greeting as planned.

#### The player gets asked for a row number between 0 and 3:
- Value between 0 and 3: Valid with a positive response.
- Value under 0: Invalid, error message "Invalid data: Only 0-3 is accepted here. You entered [number]. Please try again."
- Value over 3: Invalid, error message "Invalid data: Only 0-3 is accepted here. You entered [number]. Please try again."

- When entering invalid values the player gets the error messages above as planned and then gets to enter a new value which is correct.
- The player's guess is displayed as expected.
- If the player miss the ship it says so.
- If the player hit the ship and win it says so.
- The row and column values of the hidden ship shows in the end as it should.

# Deployment

#### The game was deployed to Heroku using the following steps

1. Once ready to deploy, commit and push all changes to GitHub.
2. Create an account on [Heroku](https://heroku.com/) if you don't have one already.
3. You then have to go to https://www.heroku.com/github-students and click on *Get the student offer*, it's possible that you have to log in to Heroku.
4. Click on *Verify with GitHub* and then on *Authorize heroku*.
5. If you don't have any saved payment details you have to do that now by clicking on *Add a credit or debit card to your account now* where you will add a card.
6. Enter your details and *Code Institute* as *School name*.
7. Agree to Heroku's terms.
8. On the Heroku dashboard you click on *Create new app*.
9. Name it to something fitting to your project, is must be unique.
10. Choose region and then click on *Create App*.
11. Under the *Settings* tab you will click on the button *Reveal Config Vars* and add the key: *PORT* with the value: *8000*.
12. Under that you have to add the buildpacks *python* and *nodejs*, it's important that they are listed in that exact order.
13. Click on the *Deploy* tab and choose GitHub as deployment method by clicking on *Connect to GitHub*.
14. Search for the GitHub repository name and then click *Connect*.
15. At the bottom of the page you click on the *Deploy bransch* button.
16.  Click on the button *View* or *Open app* at the top of the page to see the website.
17. Last step is to activate dynos by clicking on your avatar at the top right corner on Heroku and then click on *Account settings*.
18. Click on the *Billing* tab and then on the button *Subscribe to Eco* further down on the page.
19. Read the information and then click on *Subscribe*.
You now have deployed to heroku!

# Credits

- My screenshots in this README.md file is linked from [Cloudinary](https://cloudinary.com/).

Inspiration taken from the websites below:
- [Austin Montgomery](https://bigmonty12.github.io/battleship)
- [Python forum](https://python-forum.io/thread-1065.html)
- ["pranjal dev" on copyassignment.com](https://copyassignment.com/battleship-game-code-in-python/)