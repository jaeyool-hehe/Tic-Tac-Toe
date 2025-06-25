import turtle

from tkinter import messagebox

import math

from DrawingFunctions import *

from LogicFunctions import *


if __name__ == '__main__':


    boardDrawer = turtle.Turtle()
    # start place change code
    startPlaceCode(boardDrawer)
    # board drawing
    drawingBoardFunction(boardDrawer)




    # declare nine variables that represents a square.
    # Inside the variable can be None, ""O, "X"
    squareOne = None
    squareTwo = None
    squareThree = None
    squareFour = None
    squareFive = None
    squareSix = None
    squareSeven = None
    squareEight = None
    squareNine = None

    playerCircleDrawer = turtle.Turtle()
    playerXDrawer = turtle.Turtle()


    # print "* circle starts first *"
    print("* Circle starts first *")

    while True:
        # PLAYER CIRCLE TURN
        # take input and put it ina valuable called userMove
        userMoveForCircle = int(turtle.textinput("Circle",
        "Player circle, Where do do you want to place it? 1, 2, 3, 4, 5, 6, 7, 8, 9?"))

        # User move logic
        # if userMove is 1
        if userMoveForCircle == 1:
            # put "O" in squareOne
            squareOne = "O"

        # elif userMove is 2
        elif userMoveForCircle == 2:
            # put "O" in squareTwo
            squareTwo = "O"

        # elif userMove is 3
        elif userMoveForCircle == 3:
            # put "O" in squareThree
            squareThree = "O"

        # elif userMove is 4
        elif userMoveForCircle == 4:
            # put "O" in squareFour
            squareFour = "O"

        # elif userMove is 5
        elif userMoveForCircle == 5:
            # put in "O" in squareFive
            squareFive = "O"

        # elif userMove is 6
        elif userMoveForCircle == 6:
            # put in "O" in squareSix
            squareSix = "O"

        # elif userMove is 7
        elif userMoveForCircle == 7:
            # put in "O" in squareSeven
            squareSeven = "O"

        # elif userMove is 8
        elif userMoveForCircle == 8:
            # put in "O" in squareEight
            squareEight = "O"

        # elif userMove is 9
        elif userMoveForCircle == 9:
            # put in "O" in squareNine
            squareNine = "O"


        drawCircleBasedOnUserInput(userMoveForCircle, playerCircleDrawer)

        # check winning condition for circle player.
        # if isCircleWinner is True that means circle won. if isCircleWinner is false that means circle didn't win yet
        isCircleWinner = checkCircleWinningCondition(squareOne, squareTwo, squareThree,
                                             squareFour, squareFive, squareSix,
                                             squareSeven, squareEight, squareNine)
        if isCircleWinner == True:
            messagebox.showinfo("CircleWin", "Circle won!!")
            break


        # PLAYER X TURN
        # take input and put it ina valuable called userMove
        userMoveForX = int(turtle.textinput("X",
        "Player X, Where do do you want to place it? 1, 2, 3, 4, 5, 6, 7, 8, 9?"))

        # User move logic
        # if userMove is 1
        if userMoveForX == 1:
            # put "O" in squareOne
            squareOne = "X"

        # elif userMove is 2
        elif userMoveForX == 2:
            # put "O" in squareTwo
            squareTwo = "X"

        # elif userMove is 3
        elif userMoveForX == 3:
            # put "O" in squareThree
            squareThree = "X"

        # elif userMove is 4
        elif userMoveForX == 4:
            # put "O" in squareFour
            squareFour = "X"

        # elif userMove is 5
        elif userMoveForX == 5:
            # put in "O" in squareFive
            squareFive = "X"

        # elif userMove is 6
        elif userMoveForX == 6:
            # put in "O" in squareSix
            squareSix = "X"

        # elif userMove is 7
        elif userMoveForX == 7:
            # put in "O" in squareSeven
            squareSeven = "X"

        # elif userMove is 8
        elif userMoveForX == 8:
            # put in "O" in squareEight
            squareEight = "X"

        # elif userMove is 9
        elif userMoveForX == 9:
            # put in "O" in squareNine
            squareNine = "X"

        drawXBasedOnUserInput(userMoveForX, playerXDrawer)

        # Check winning condition for X player.
        # if isXWinner is True that means X won. if isXWinner is false that means X didn't win yet.
        isXWinner = checkXWinningCondition(squareOne, squareTwo, squareThree,
                               squareFour, squareFive, squareSix,
                               squareSeven, squareEight, squareNine)

        if isXWinner == True:
            messagebox.showinfo("XWin", "X won!!")
            break




    # outside of the while loop
    turtle.done()