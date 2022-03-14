from random import randint
from collections import Counter


class GameLogic:

    @staticmethod
    def calculate_score(rolls):
        """
        This function takes a tuple represents the rolls
        of dices (0 ~ 6), and return the score based on
        the rules of the game of greed
        """

        score = 0       # current score for this round
        excluded = 0        # the number we want to delte from the list after recording its score
        counts_list = Counter(rolls).most_common()  # counts of rolls

        # if the rolls list is not empty, define the excluded item as the one with most occurences
        # otherwise, return the score as 0
        if len(rolls) != 0:
            excluded = counts_list[0][0]
        else:
            return score        # it is (0)

        # go through every possible repeatetion and record the score for it
        if (counts_list[0][1] == 1) and (len(rolls) == 6):
            return 1500
        elif (counts_list[0][1] == 2) and (len(counts_list) == 3) and (len(rolls) == 6):
            if counts_list[1][1] == 2:
                return 1500
        elif (counts_list[0][1] == 3) and (len(counts_list) == 2) and (len(rolls) == 6):
            if counts_list[1][1] == 3:
                return 1200
        elif (counts_list[0][1] == 6) and (len(counts_list) == 1):
            return 4000 if counts_list[0][0] == 1 else 400 * counts_list[0][0]       
        else:
            if counts_list[0][1] == 5:
                score = score + (3000 if counts_list[0][0] == 1 else 300 * counts_list[0][0])        
            elif counts_list[0][1] == 4:
                score = score + (2000 if counts_list[0][0] == 1 else 200 * counts_list[0][0])
            elif counts_list[0][1] == 3:
                score = score + (1000 if counts_list[0][0] == 1 else 100 * counts_list[0][0])
            elif counts_list[0][1] == 2:
                score = score + (200 if counts_list[0][0] == 1 else 100 if counts_list[0][0]==5 else 0)
            elif counts_list[0][1] == 1:
                score = score + (100 if counts_list[0][0] == 1 else 50 if counts_list[0][0]==5 else 0)
    
        # delete all the occurences of the defined (excluded) item and put the rest in a new list
        rolls = tuple([i for i in rolls if i != excluded])

        # if there are any items left in the list after deletions, re call the function with that list,
        #   then add the returned value to the curren score  
        if len(rolls) != 0:
            score += GameLogic.calculate_score(rolls)
        
        return score


    @staticmethod
    def roll_dice(dices):
        """
        This function simulates a dice roll, it's repeated
        (dices) of times and return a tuple of results
        """

        return tuple([randint(1, 6) for _ in range(dices)])


if __name__ == "__main__":
    print(GameLogic.calculate_score((4,6)))