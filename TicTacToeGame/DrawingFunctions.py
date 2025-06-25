import math




def startPlaceCode(boardDrawer):
    # start place change code
    boardDrawer.penup()
    boardDrawer.left(90)
    boardDrawer.forward(90)
    boardDrawer.left(90)
    boardDrawer.forward(90)
    boardDrawer.left(180)
    boardDrawer.pendown()

def drawingBoardFunction(boardDrawer):

    # Base board drawing code
    boardDrawer.forward(270)
    boardDrawer.right(90)
    boardDrawer.forward(270)
    boardDrawer.right(90)
    boardDrawer.forward(270)
    boardDrawer.right(90)
    boardDrawer.forward(270)

    # vertical small board drawing code
    boardDrawer.right(90)
    boardDrawer.forward(90)
    boardDrawer.right(90)
    boardDrawer.forward(270)
    boardDrawer.left(90)
    boardDrawer.forward(90)
    boardDrawer.left(90)
    boardDrawer.forward(270)

    # horizontal small board drawing code
    boardDrawer.right(90)
    boardDrawer.forward(90)
    boardDrawer.right(90)
    boardDrawer.forward(90)
    boardDrawer.right(90)
    boardDrawer.forward(270)
    boardDrawer.left(90)
    boardDrawer.forward(90)
    boardDrawer.left(90)
    boardDrawer.forward(270)


def drawX(playerXDrawer, coordinateX, coordinateY, size):
    playerXDrawer.teleport(coordinateX, coordinateY)
    playerXDrawer.left(45)
    playerXDrawer.forward(size)
    playerXDrawer.backward(size)
    playerXDrawer.penup()
    playerXDrawer.left(45)
    playerXDrawer.forward(size / math.sqrt(2))
    playerXDrawer.pendown()
    playerXDrawer.right(135)
    playerXDrawer.forward(size)
    playerXDrawer.left(45)

def drawCircle(playerCircleDrawer, coordinateX, coordinateY, radius):
    playerCircleDrawer.teleport(coordinateX, coordinateY)
    playerCircleDrawer.circle(radius)


def drawXBasedOnUserInput(userMove, playerXDrawer):
    if userMove == 1:
        drawX(playerXDrawer, -50, 50, 20)

    elif userMove == 2:
        drawX(playerXDrawer, 50, 50, 20)

    elif userMove == 3:
        drawX(playerXDrawer, 120, 50, 20)

    elif userMove == 4:
        drawX(playerXDrawer, -50, -50, 20)

    elif userMove == 5:
        drawX(playerXDrawer, 50, -50, 20)

    elif userMove == 6:
        drawX(playerXDrawer, 120, -50, 20)

    elif userMove == 7:
        drawX(playerXDrawer, -50, -120, 20)

    elif userMove == 8:
        drawX(playerXDrawer, 50, -120, 20)

    elif userMove == 9:
        drawX(playerXDrawer, 120, -120, 20)


def drawCircleBasedOnUserInput(userMove, playerCircleDrawer):
    if userMove == 1:
        drawCircle(playerCircleDrawer, -50, 50, 10)

    elif userMove == 2:
        drawCircle(playerCircleDrawer, 50, 50, 10)

    elif userMove == 3:
        drawCircle(playerCircleDrawer, 120, 50, 10)

    elif userMove == 4:
        drawCircle(playerCircleDrawer, -50, -50, 10)

    elif userMove == 5:
        drawCircle(playerCircleDrawer, 50, -50, 10)

    elif userMove == 6:
        drawCircle(playerCircleDrawer, 120, -50, 10)

    elif userMove == 7:
        drawCircle(playerCircleDrawer, -50, -120, 10)

    elif userMove == 8:
        drawCircle(playerCircleDrawer, 50, -120, 10)

    elif userMove == 9:
        drawCircle(playerCircleDrawer, 120, -120, 10)


