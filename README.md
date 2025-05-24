Used to share the code of the final project in the usyd 9001 course

The following are the detailed rules of this game:
In this version of game, both players will draw cards from a custom deck that contains only 13 unique cards, representing the standard ranks from A to K. The card values are as follows:

A = 1  
J = 11  
Q = 12  
K = 13  
All other numbered cards retain their face values.
Each card appears only once in the deck, so no duplicate cards will be drawn during the game.

Game Mechanics:  
At the start of each game round, the system deals one hidden card (a hole card) to both the player and the computer. This card is not revealed to the opponent.
Then, both players take turns deciding whether to Hit (draw a card) or Stand (end their turn).
All cards drawn after the initial hole card are face-up (visible to both sides).
Once a player chooses to Stand, they can no longer draw any more cards and must wait for the round to conclude.
When both players have chosen to Stand, the game proceeds to resolution.


Win Conditions:  
If one player busts (goes over 21) and the other does not, the player who did not bust wins.

If both players are under or equal to 21, the hand closer to 21 wins.

If both players have the same hand value, or if both bust, the round ends in a tie. In the case where both bust, their actual values are not compared.
  
Card Dealing:  
All cards are dealt completely at random from the 13-card deck.   
                                

AI Logic:  
The computer-controlled player will assess the probability of busting based on the remaining cards in the deck and its current hand value.
The higher the chance of busting with the next draw, the less likely it is to Hit; conversely, it will be more inclined to Hit when the bust risk is lower.
The computer does not know the player’s hidden card.


Input Format：  
The input does not matter if it is upper or lower case, but the spelling must be correct.
