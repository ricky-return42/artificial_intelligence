<img src='http://www.zumodecolores.com/160-470-thickbox/tres-en-raya.jpg'>

Exploration of artificial intelligence in nought and crosses

#### AI idea

AI is trained in a Monte Carlo style. The computer plays a large number of games with random moves against itself. Board positions and end results were logged for each move. By dividing the number of appearance in won games by the total appearances, the winning probabilities of the specific board positions are calculated. Then a 'smart' computer can play against human and pick its move according to its experience (the winning probabilities calculated earlier).This proves to be in many cases an effective solution for this game.

For entertaitment purpose, 2-players game is also available.


#### How to use/play

1. Run the first cell in the notebook
2. Select the number of training iterations and run the second cell. It requires as many as 20000 cycles for the AI to learn properly
3. Run the third cell to play the game
> - fill in 'smart' parameter (default = None). This option determines which computer player is 'smart'. It is very obvious that a smart computer outplays a random computer easily
> - Choose number of players: if set to 0, then a demonstration between computer AIs will be shown
