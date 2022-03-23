from re import T
from game_of_greed.banker import Banker
from game_of_greed.game_logic import GameLogic


class Game:

    def __init__(self, roller=GameLogic.roll_dice):
        self.roller = roller
        self.rounds = 0
        self.banker = Banker()


    def play(self):
        """
        This function starts the game of greed 
        """
 
        quited = False      # this is for the outer while-loop to control when do we want to quit the game
        num_dice = 6        # this is for keep tracking the current number of dice
        # print("Welcome to Game of Greed")
        print("(y)es to play or (n)o to decline")
        answer_1 = input("(y)es to play or (n)o to decline")
        # if the answer is "n", quit the whole game and print the thanks-
        if answer_1 == "n":
            print("OK. Maybe another time")
            return
        # if the answer is anything else, start the round 1

        # this outer loop is for looping through "rounds"
        while not quited:
            if self.__check_for_10000(): 
                break
            self.rounds += 1                            # increment the round counter
            num_dice = 6                                # reset the number of dice
            print(f"Starting round {self.rounds}")      # print the round counter

            # this first inner while-loop is for looping through rolling dice in a "single round"
            while True:
                if self.__check_for_10000(): 
                    quited = True
                    break
                print(f"Rolling {num_dice} dice...")                    # print the number of dice we have now
                rolled_dice = self.roller(num_dice)                     # roll the set of dice 
                rolled_dice_strings = [str(i) for i in rolled_dice]     # cast the integers to strings
                print(f"*** {','.join(rolled_dice_strings)}")                    # print the rolled dice
                
                # Is it a Zilch ? if the calculated score is equal to zero, then it is ! 
                score_now = GameLogic.get_scorers(tuple(rolled_dice), custom=True)                
                if score_now == 0:
                    print(f"Zilch!!! Round over\nYou banked 0 points in round {self.rounds}\nTotal score is {self.banker.balance} points")
                    self.banker.clear_shelf()
                    break
                
                # Anti-cheat-loop: this second inner while-loop is for keep looping untill the user provide a valid input
                while True:
                    print("Enter dice to keep, or (q)uit:")
                    answer_2 = input("Enter dice to keep, or (q)uit:")
                    if answer_2 == "q": break                       # if user wants to quit, break both inner loops
                    dice_remaining = [j for j in rolled_dice]       # make a copy so we dont lose the original
                    cheater_state = False                           # to track if the user cheated or made a typo
                    # loop through the user's input char by char
                    for char in answer_2:
                        # check if any of them is not a digit, and print the cheating sentence if one is not
                        if not char.isdigit():
                            print(f"Cheater!!! Or possibly made a typo...\n*** {','.join(rolled_dice_strings)}")
                            cheater_state = True
                            break
                        # keep checking if one of the elements isn't in the list and remove it if it is 
                        # if any of them is not in the list -after removal-, print the cheating sentence
                        if int(char) in dice_remaining:
                            dice_remaining.remove(int(char))
                        else:
                            print(f"Cheater!!! Or possibly made a typo...\n*** {','.join(rolled_dice_strings)}")
                            cheater_state = True
                            break
                    # if we have a cheating case, keep looping 
                    if cheater_state:
                        continue
                    # if tou reached this line, then we didn't have cheating and you're free to complete the game 
                    break

                # if the user decided to quit during the last loop, break the round's loop
                if answer_2 == "q":
                    print(f"Total score is {self.banker.balance} points") if (self.banker.balance!=0) or (self.rounds!=1) else None
                    quited = True
                    break

                answer_2 = tuple([int(i) for i in answer_2])            # cast the valid input into a tuple of integers
                points = GameLogic.get_scorers(tuple(answer_2), custom=True)     # calculate the score 
                self.banker.shelf(points)                               # self the points
                print(f"You have {self.banker.shelved} unbanked points and {len(dice_remaining)} dice remaining")
                print("(r)oll again, (b)ank your points or (q)uit:")
                answer_3 = input("(r)oll again, (b)ank your points or (q)uit:")

                # if the user wants to roll, go to the next "roll" of the same round
                if answer_3 == "r":
                    if len(dice_remaining) == 0:
                        num_dice = 6
                        continue
                    num_dice = len(dice_remaining)
                    continue
                # if the user wants to bank, store his shelved points, then go to the next "round"
                elif answer_3 == "b":
                    print(f"You banked {self.banker.shelved} points in round {self.rounds}")
                    self.banker.bank()
                    print(f"Total score is {self.banker.balance} points")
                    break
                # if the user wants to quit, then close both inner and outer loops
                else:
                    print(f"Total score is {self.banker.balance} points")
                    quited = True
                    break

        print(f"Thanks for playing. You earned {self.banker.balance} points")


    def __check_for_10000(self):
        if self.banker.balance >= 10000:
            return True  
        else: 
            return False
             



if __name__ == "__main__":
    from game_of_greed.game_logic import GameLogic
    game = Game()
    game.play()



