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
 
        quited = False      # this is for the first outer while-loop to control when do we want to quit the game
        num_dice = 6        # this is for keep tracking the current number of dice
        zilch_or_cheat = False

        # welcome message with the first question
        print("Welcome to Game of Greed")
        answer_1 = input("Wanna play? ")
        
        # if the answer is "n", quit the whole game and print the thanks-
        if answer_1 == "n":
            print("OK. Maybe another time")
            return

        # if the answer is anything else, start the round 1
        # the outer loop is for looping through "rounds"
        while not quited:
            self.rounds += 1                            # increment the round counter
            num_dice = 6                                # reset the number of dice
            print(f"Starting round {self.rounds}")      # print the round counter

            # the inner loop is for looping through rolling dice in a single round
            while True:
                print(f"Rolling {num_dice} dice...")    # print the number of dice we have now
                rolled_dice = self.roller(num_dice)     # roll the set of dice 
                rolled_dice_strings = [str(i) for i in rolled_dice]
                print(','.join(rolled_dice_strings))

                # if the calculated score is equal to zero, then it is zilch 
                if GameLogic.calculate_score(tuple(rolled_dice)) == 0:
                    print("Zilch!!! Round over")
                    print(f"You banked 0 points in round {self.rounds}")
                    self.banker.clear_shelf()
                    print(f"Total score is {self.banker.balance} points")
                    zilch_or_cheat = True
                    break
                
                while True:
                    answer_2 = input("Enter dice to keep (no spaces), or (q)uit: ")
                    if answer_2 == "q": break
                    rolled_dice_copy = [j for j in rolled_dice]

                    cheater_state = False
                    for i in answer_2:
                        if not i.isdigit():
                            Game.cheater(rolled_dice_strings)
                            zilch_or_cheat = True
                            cheater_state = True
                            break

                        if int(i) in rolled_dice_copy:
                            rolled_dice_copy.remove(int(i))
                        else:
                            Game.cheater(rolled_dice_strings)
                            zilch_or_cheat = True
                            cheater_state = True
                            break
                        
                    if cheater_state:
                        continue

                    break

                if answer_2 == "q":
                    if (self.banker.balance != 0) or (zilch_or_cheat): 
                        print(f"Total score is {self.banker.balance} points")
                    quited = True
                    break

                answer_2 = tuple([int(i) for i in answer_2]) 
                points = GameLogic.calculate_score(tuple(answer_2))
                self.banker.shelf(points)
                dice_remaining = [k for k in rolled_dice_copy]
                print(f"You have {self.banker.shelved} unbanked points and {len(dice_remaining)} dice remaining")
                answer_3 = input("(r)oll again, (b)ank your points or (q)uit ")

                if answer_3 == "r":
                    if len(dice_remaining) == 0:
                        num_dice = 6
                        continue
                    num_dice = len(dice_remaining)
                    continue
                elif answer_3 == "b":
                    print(f"You banked {self.banker.shelved} points in round {self.rounds}")
                    self.banker.bank()
                    print(f"Total score is {self.banker.balance} points")
                    break
                else:   # q
                    if (self.banker.balance != 0) or (zilch_or_cheat):
                        print(f"Total score is {self.banker.balance} points")
                    quited = True
                    break

        print(f"Thanks for playing. You earned {self.banker.balance} points")


    @staticmethod
    def cheater(dice):
        print("Cheater!!! Or possibly made a typo...")
        print(','.join(dice))

                            

if __name__ == "__main__":
    from game_of_greed.game_logic import GameLogic
    game = Game()
    game.play()
