#Thomas Matlak
#CSCI100 Final Project
#22 November 2014
#This program runs the game Tic-Tac-Toe for one or two players
#TODO:
#Pretty up the game
#Refactor

from Tkinter import *
import random
import sys

#Draws the tic-tac-toe board
def drawBoard(window):
    for i in range(2, 5, 2):
        window.create_line(i * 100, 0, i * 100, 600)
        window.create_line(0, i * 100, 600, i * 100)

#Global variables for the players to determine who has won and whose turn it is
availablePlaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player1Places = []
player2Places = []

#Draws an X beginning at the upper left corner of the given position
def drawX(window, position):
    window.create_line(position[0], position[1], position[0] + 200, position[1] + 200, width=2)
    window.create_line(position[0] + 200, position[1], position[0], position[1] + 200, width=2)
    
#Draws an O beginning at the upper left corner of the given position
def drawO(window, position):
    window.create_oval(position[0], position[1], position[0] + 200, position[1] + 200, width=2)

#Returns where to place the x or o and which section of the grid that is
def pieceLocation(clickCoordinate):
    x = clickCoordinate[0]
    y = clickCoordinate[1]
    
    if x < 200 and y < 200:
        return ((0, 0), 1)
    elif x < 200 and y > 200 and y < 400:
        return ((0, 200), 2)
    elif x < 200 and  y > 400:
        return ((0, 400), 3)
    elif x > 200 and x < 400 and y < 200:
        return ((200, 0), 4)
    elif x > 200 and x < 400 and y > 200 and y < 400:
        return ((200, 200), 5)
    elif x > 200 and x < 400 and y > 400:
        return ((200, 400), 6)
    elif x > 400 and y < 200:
        return ((400, 0), 7)
    elif x >400 and y > 200 and y < 400:
        return ((400, 200), 8)
    elif x >400 and y > 400:
        return ((400, 400), 9)

#Determine whether a player has won
def checkHasWon(piecePlaces):
    if (1 in piecePlaces and 4 in piecePlaces and 7 in piecePlaces) or \
    (2 in piecePlaces and 5 in piecePlaces and 8 in piecePlaces) or \
    (3 in piecePlaces and 6 in piecePlaces and 9 in piecePlaces) or \
    (1 in piecePlaces and 2 in piecePlaces and 3 in piecePlaces) or \
    (4 in piecePlaces and 5 in piecePlaces and 6 in piecePlaces) or \
    (7 in piecePlaces and 8 in piecePlaces and 9 in piecePlaces) or \
    (1 in piecePlaces and 5 in piecePlaces and 9 in piecePlaces) or \
    (3 in piecePlaces and 5 in piecePlaces and 7 in piecePlaces):
        return True
    else:
        return False

#Takes the mouse coordinates when player 1 makes a move
def onClickInGame1(event, numPlayers, first, player):
    coordinates = pieceLocation((event.x, event.y))
    if coordinates[1] in availablePlaces:
        drawX(boardWindow, coordinates[0])
        player1Places.append(coordinates[1])
        availablePlaces.remove(coordinates[1])
        player = 3 - player
    else:
        player = player
        print "That spot is already taken"
    ticTacToe(player, numPlayers, first)

#Takes the mouse coordinates when player 2 makes a move
def onClickInGame2(event, numPlayers, first, player):
    coordinates = pieceLocation((event.x, event.y))
    if coordinates[1] in availablePlaces:
        drawO(boardWindow, coordinates[0])
        player2Places.append(coordinates[1])
        availablePlaces.remove(coordinates[1])
        player = 3 - player
    else:
        player = player
        print "That spot is already taken"
    ticTacToe(player, numPlayers, first)

#Makes a move for the ai using the random package
def aiMove(aiPlayer, first):
    coordinates = pieceLocation((random.randrange(600), random.randrange(600)))
    if coordinates[1] in availablePlaces:
        if first == "X":
            drawO(boardWindow, coordinates[0])
        elif first == "O":
            drawX(boardWindow, coordinates[0])
        if aiPlayer == 1:
            player1Places.append(coordinates[1])
        elif aiPlayer == 2:
            player2Places.append(coordinates[1])
        availablePlaces.remove(coordinates[1])
        player = 3 - aiPlayer
    else:
        player = aiPlayer
    ticTacToe(player, 1, first)

#Exits the program onclick
def exitClick(event):
    sys.exit()

def drawLine(player1Places, player2Places):
    if checkHasWon(player1Places):
        if (1 in player1Places and 4 in player1Places and 7 in player1Places):
            boardWindow.create_line(0, 100, 600, 100, fill="red", width=5)
        elif (2 in player1Places and 5 in player1Places and 8 in player1Places):
            boardWindow.create_line(0, 300, 600, 300, fill="red", width=5)
        elif (3 in player1Places and 6 in player1Places and 9 in player1Places):
            boardWindow.create_line(0, 500, 600, 500, fill="red", width=5)
        elif (1 in player1Places and 2 in player1Places and 3 in player1Places):
            boardWindow.create_line(100, 0, 100, 600, fill="red", width=5)
        elif (4 in player1Places and 5 in player1Places and 6 in player1Places):
            boardWindow.create_line(300, 0, 300, 600, fill="red", width=5)
        elif (7 in player1Places and 8 in player1Places and 9 in player1Places):
            boardWindow.create_line(500, 0, 500, 600, fill="red", width=5)
        elif (1 in player1Places and 5 in player1Places and 9 in player1Places):
            boardWindow.create_line(0, 0, 600, 600, fill="red", width=5)
        elif (3 in player1Places and 5 in player1Places and 7 in player1Places):
            boardWindow.create_line(0, 600, 600, 0, fill="red", width=5)
    if checkHasWon(player2Places):
        if (1 in player2Places and 4 in player2Places and 7 in player2Places):
            boardWindow.create_line(0, 100, 600, 100, fill="red", width=5)
        elif (2 in player2Places and 5 in player2Places and 8 in player2Places):
            boardWindow.create_line(0, 300, 600, 300, fill="red", width=5)
        elif (3 in player2Places and 6 in player2Places and 9 in player2Places):
            boardWindow.create_line(0, 500, 600, 500, fill="red", width=5)
        elif (1 in player2Places and 2 in player2Places and 3 in player2Places):
            boardWindow.create_line(100, 0, 100, 600, fill="red", width=5)
        elif (4 in player2Places and 5 in player2Places and 6 in player2Places):
            boardWindow.create_line(300, 0, 300, 600, fill="red", width=5)
        elif (7 in player2Places and 8 in player2Places and 9 in player2Places):
            boardWindow.create_line(500, 0, 500, 600, fill="red", width=5)
        elif (1 in player2Places and 5 in player2Places and 9 in player2Places):
            boardWindow.create_line(0, 0, 600, 600, fill="red", width=5)
        elif (3 in player2Places and 5 in player2Places and 7 in player2Places):
            boardWindow.create_line(0, 600, 600, 0, fill="red", width=5)

#Checks if the game is over. If not, lets the next player make a move
def ticTacToe(player, numPlayers, first):
    if checkHasWon(player1Places) or checkHasWon(player2Places):
        if numPlayers == 2:
            drawLine(player1Places, player2Places)
            print "Congratulations Player ", 3 - player, "!"
        elif numPlayers == 1 and checkHasWon(player1Places) and first == "X":
            drawLine(player1Places, player2Places)
            print "Congratulations!"
        elif numPlayers == 1 and checkHasWon(player2Places) and first == "O":
            drawLine(player1Places, player2Places)
            print "Congratulations!"
        elif numPlayers == 1 and checkHasWon(player1Places) and first == "O":
            drawLine(player1Places, player2Places)
        elif numPlayers == 1 and checkHasWon(player2Places) and first == "X":
            drawLine(player1Places, player2Places)
        boardWindow.bind("<Button-1>", exitClick)
    elif availablePlaces == []:
        print "Tie Game"
        boardWindow.bind("<Button-1>", exitClick)
    elif not checkHasWon(player1Places) and not checkHasWon(player2Places):
        #Take user input for which location to place their piece or makes the computer's move
        if player == 1:
            if numPlayers == 1 and first == "X":
                boardWindow.bind("<Button-1>", lambda event: onClickInGame1(event, numPlayers, first, player))
            elif numPlayers == 1 and first == "O":
                aiMove(player, first)
            elif numPlayers == 2:
                boardWindow.bind("<Button-1>", lambda event: onClickInGame1(event, numPlayers, first, player))
        elif player == 2:
            if numPlayers == 1 and first == "X":
                aiMove(player, first)
            elif numPlayers == 1 and first == "O":
                boardWindow.bind("<Button-1>", lambda event: onClickInGame2(event, numPlayers, first, player))
            elif numPlayers == 2:
                boardWindow.bind("<Button-1>", lambda event: onClickInGame2(event, numPlayers, first, player))
        
    mainloop()

#Get number of players
numPlayers = int(raw_input("How many players?: "))
if numPlayers == 1:
    symbol = raw_input("Would you like to be X or O?: ")
    first = symbol.upper()
elif numPlayers == 2:
    first = "X"

#Creates the window for the game
root = Tk()
boardWindow = Canvas(root, width = 600, height = 600)
boardWindow.pack()
drawBoard(boardWindow)

#Run the game
ticTacToe(1, numPlayers, first)