from game_of_greed.banker import Banker
from game_of_greed.game_logic import GameLogic


class Game:
    def __init__(self, roller=None):
        self.roller = roller
        self.rounds = 0
        self.quited = False
        self.banker = Banker()


    def play(self):
        print("Welcome to Game of Greed")
        answer_1 = input("Wanna play? ")
        
        if answer_1 == "n":
            print("OK. Maybe another time")
            return 0

        else:   # y
            while not self.quited:
                self.rounds += 1
                print(f"Starting round {self.rounds}")

                while True:
                    print("Rolling 6 dice...")

                    rolled_dice = self.roller(6)
                    rolled_dice_strings = [str(i) for i in rolled_dice]
                    print(','.join(rolled_dice_strings))
                    # print(*rolled_dice_strings , sep=',')

                    answer_2 = input("Enter dice to keep (no spaces), or (q)uit: ")

                    if answer_2 == "q":
                        if self.banker.balance != 0:
                            print(f"Total score is {self.banker.balance} points")
                        self.quited = True
                        break
                    else:   # numbers
                        answer_2 = tuple([int(i) for i in answer_2]) 
                        points = GameLogic.calculate_score(tuple(answer_2))
                        self.banker.shelf(points)

                        dice_remaining = len(rolled_dice) - len(answer_2)

                        print(f"You have {self.banker.shelved} unbanked points and {dice_remaining} dice remaining")

                        answer_3 = input("(r)oll again, (b)ank your points or (q)uit ")

                        if answer_3 == "r":
                            continue
                        elif answer_3 == "b":
                            print(f"You banked {self.banker.shelved} points in round {self.rounds}")
                            self.banker.bank()
                            print(f"Total score is {self.banker.balance} points")
                            break
                        else:   # q
                            print(f"Total score is {self.banker.balance} points")
                            self.quited = True
                            break
                            

        print(f"Thanks for playing. You earned {self.banker.balance} points")
                            



if __name__ == "__main__":
    from game_of_greed.game_logic import GameLogic
    game = Game(GameLogic.roll_dice)
    game.play()

