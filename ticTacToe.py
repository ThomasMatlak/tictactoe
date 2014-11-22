#Thomas Matlak
#CSCI100 Final Project
#22 November 2014
#This program runs the game Tic-Tac-Toe for two players
#TODO:
#-Add 1 player mode
#--select screen
#--AI for 1 player using random

from Tkinter import *
import random
import sys

#Draws the tic-tac-toe board
def drawBoard(window):
    for i in range(2, 5, 2):
        window.create_line(i * 100, 0, i * 100, 600)
        window.create_line(0, i * 100, 600, i * 100)
        
root = Tk()
boardWindow = Canvas(root, width = 600, height = 600)
boardWindow.pack()
drawBoard(boardWindow)

availablePlaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player1Places = []
player2Places = []
player = 1

#Draws an X beginning at the upper left corner of the given position
def drawX(window, position):
    window.create_line(position[0], position[1], position[0] + 200, position[1] + 200)
    window.create_line(position[0] + 200, position[1], position[0], position[1] + 200)
    
#Draws an O beginning at the upper left corner of the beginning position
def drawO(window, position):
    window.create_oval(position[0], position[1], position[0] + 200, position[1] + 200)

#Returns where to place the x or o and which part of the grid that is
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

#Take the mouse coordinates on click
def onClickInGame1(event):
    coordinates = pieceLocation((event.x, event.y))
    if coordinates[1] in availablePlaces:
        drawX(boardWindow, coordinates[0])
        player1Places.append(coordinates[1])
        availablePlaces.remove(coordinates[1])
        player = 2
    else:
        player = 1
        print "That spot is already taken"
    ticTacToe(player)

def onClickInGame2(event):
    coordinates = pieceLocation((event.x, event.y))
    if coordinates[1] in availablePlaces:
        drawO(boardWindow, coordinates[0])
        player2Places.append(coordinates[1])
        availablePlaces.remove(coordinates[1])
        player = 1
    else:
        player = 2
        print "That spot is already taken"
    ticTacToe(player)

def ticTacToe(player):
    if checkHasWon(player1Places) or checkHasWon(player2Places):
        print "Congratulation Player ", 3 - player, "!"
        sys.exit()
    elif availablePlaces == []:
        print "Tie Game"
        sys.exit()
    elif checkHasWon(player1Places) == False and checkHasWon(player2Places) == False:
        #Take user input for which location to place their piece
        if player == 1:
            boardWindow.bind("<Button-1>", onClickInGame1)
        elif player == 2:
            boardWindow.bind("<Button-1>", onClickInGame2)
        
    mainloop()

ticTacToe(player)