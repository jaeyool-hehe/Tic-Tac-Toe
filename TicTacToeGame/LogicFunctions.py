from DrawingFunctions import *



def checkCircleWinningCondition(squareOne, squareTwo, squareThree,
                                squareFour, squareFive, squareSix,
                                squareSeven, squareEight, squareNine):
    # we want to have the game logic that checks for win condition
    # horizontal winning conditions
    if squareOne == "O" and squareTwo == "O" and squareThree == "O":
        return True
    elif squareFour == "O" and squareFive == "O" and squareSix == "O":
        return True
    elif squareSeven == "O" and squareEight == "O" and squareNine == "O":
        return True

    # vertical winning conditions
    elif squareOne == "O" and squareFour == "O" and squareSeven == "O":
        return True
    elif squareTwo == "O" and squareFive == "O" and squareEight == "O":
        return True
    elif squareThree == "O" and squareSix == "O" and squareNine == "O":
        return True

    # diagonal winning conditions
    elif squareOne == "O" and squareFive == "O" and squareNine == "O":
        return True
    elif squareThree == "O" and squareFive == "O" and squareSeven == "O":
        return True
    else:
        return False

def checkXWinningCondition(squareOne, squareTwo, squareThree,
                                squareFour, squareFive, squareSix,
                                squareSeven, squareEight, squareNine):
    # we want to have the game logic that checks for win condition
    # horizontal winning conditions
    if squareOne == "X" and squareTwo == "X" and squareThree == "X":
        return True
    elif squareFour == "X" and squareFive == "X" and squareSix == "X":
        return True
    elif squareSeven == "X" and squareEight == "X" and squareNine == "X":
        return True

    # vertical winning conditions
    elif squareOne == "X" and squareFour == "X" and squareSeven == "X":
        return True
    elif squareTwo == "X" and squareFive == "X" and squareEight == "X":
        return True
    elif squareThree == "X" and squareSix == "X" and squareNine == "X":
        return True

    # diagonal winning conditions
    elif squareOne == "X" and squareFive == "X" and squareNine == "X":
        return True
    elif squareThree == "X" and squareFive == "X" and squareSeven == "X":
        return True
    else:
        return False



