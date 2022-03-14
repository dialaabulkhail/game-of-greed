# Game of Greed
Game of greed is a game where each player competes to be the first to reach 10,000 points.

## Group 2 team:

 - Mustafa Alhasanat
 - Diala Abul-Khail
 - Abedalqader Alkhatib
 - Eman Al-Shaikh Hussain
 
## Overview

This lab is about tackling the highest risk and/or highest priority features - scoring, dice rolling and banking of points.

- Players can choose to reroll all six dice, losing their initial score in the hopes of scoring a higher one.

- Players can choose to save some of the dice already in a scoring position to attempt to make a higher score with the remaining dice. However, if a higher score isn’t achieved with the reroll, the player scores 0 for the turn.

[Game rules](https://en.wikipedia.org/wiki/Dice_10000)

## Lab requirements
- Create a game_logic class -> to handle calculating score for dice roll.

- Create a Banker class -> to add and remove score from shelf.

**Testing**
1. zilch - roll with no scoring dice should return 0
2. ones - rolls with various number of 1s should return correct score
3. twos - rolls with various number of 2s should return correct score
4. threes - rolls with various number of 3s should return correct score
5. fours - rolls with various number of 4s should return correct score
6. fives - rolls with various number of 5s should return correct score
7. sixes - rolls with various number of 6s should return correct score
8. straight - 1,2,3,4,5,6 should return correct score
9. three_pairs - 3 pairs should return correct score
10. two_trios - 2 sets of 3 should return correct score
11. leftover_ones - 1s not used in set of 3 (or greater) should return 12. correct score
14. leftover_fives - 5s not used in set of 3 (or greater) should 
15. return correct score


## API

- calculate_score() --> a class method that calculates score based on a tuple input of a dice roll.

- roll_dice() --> a class method that returns a tuple with random values between 1 and 6 . The length of tuple matches the argument passed in the method.

- shelf() --> This method receives arguments of points (integer), to add to the shelf.
shelf method temporarily store unbanked points.

- bank() --> This method adds any points on the shelf to the total(balance) and reset shelf to 0.
the output of the bank method is the amount of points added to total(balance) from shelf.

- clear_shelf() --> This method removes all unbanked points.