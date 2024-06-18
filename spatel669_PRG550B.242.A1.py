

# Your solution may ONLY use the python modules listed below
# program: spatel669_PRG550B.242.A1.py
# author:  Smit Patel
# date:    june 18th, 2024
# purpose: python main( ) program for PRG550 SUMMER 2024 Assignment #1
# version: 1.00
# reference: danny abedris

import math
import random
import string
import collections
import datetime
import re
import time
import copy


def generateGameBoard(nRows, nCols) :
    number = []
    for i in range(10,36):
        number.append(i)
    
    if (nRows in number) and (nCols in number):
        board = [['~' for j in range(nCols)]for i in range(nRows)]
        return board
    
    else:
        print('Rows and Columns should between 10 to 35')
      
   
# end def
def loadShip(boardData, nRows, nCols, coord, ship):
    if len(coord) != 2:
        return False

    else: 
        labels = "123456789" + string.ascii_uppercase
        row_index = labels.index(coord[0])
        col_index = labels.index(coord[1])
        
        index = 0
        
        while (index <= (len(ship) - 1)) :
            boardData[row_index][col_index + index] = ship[index]
            index = index + 1
            
        return boardData

# end def

def checkCoord(nRows, nCols, coord):
    if len(coord) != 2:
        return False
    
    if coord.isalnum() :
        
        labels = "123456789" + string.ascii_uppercase
        row_index = labels.index(coord[0])
        col_index = labels.index(coord[1])
    
        if 0 <= row_index < nRows and 0 <= col_index < nCols:
            return True
        else:
            return False
    else: 
        return False
# end def

def updateGameBoard(boardData, boardMask, nRows, nCols, coord, score, lastMove):
    labels = "123456789" + string.ascii_uppercase
    
    if checkCoord(nRows, nCols, coord):
        row_index = labels.index(coord[0])
        col_index = labels.index(coord[1])

        if boardData[row_index][col_index] != '~' and boardData[row_index][col_index] != 'X':
            
            char = boardData[row_index][col_index]
            boardMask[row_index][col_index] = char
            increment_index = 0
            decrement_index = -1

            while (col_index + increment_index < nCols and boardData[row_index][col_index + increment_index] != '~'):
               boardMask[row_index][col_index + increment_index] = boardData[row_index][col_index + increment_index]
               increment_index += 1
               score += 5

            while (col_index + decrement_index >= 0 and boardData[row_index][col_index + decrement_index] != '~'):
               boardMask[row_index][col_index + decrement_index] = boardData[row_index][col_index + decrement_index]
               decrement_index -= 1
               score += 5

            print("  Python Battleship@Seneca...")
            print("  " + labels[:nCols])

            for i in range(nRows):
               print(labels[i] + "|" + ''.join(("%s" % x) for x in boardMask[i]) + "|")

            print(f"Current Score:{score:03} Last Move: Torpedo HIT \'{char}\' at ", end = "")
            print(f"[{coord[0]},{coord[1]}]")

            lastMove = f"Torpedo HIT {char} at [{coord[0]},{coord[1]}]"
            return boardData, boardMask, score , lastMove

        else:
            boardMask[row_index][col_index] = 'X'

            print("  Python Battleship@Seneca...")
            print("  " + labels[:nCols])

            for i in range(nRows):
                print(labels[i] + "|" + ''.join(("%s" % x) for x in boardMask[i]) + "|")

            print(f"Current Score:{score:03} Last Move: Torpedo MISS at ", end = "")
            print(f"[{coord[0]},{coord[1]}]")

            lastMove = f"Torpedo MISS at [{coord[0]},{coord[1]}]"
            return boardData, boardMask, score, lastMove

    else:

        print("  Python Battleship@Seneca...")
        print("  " + labels[:nCols])

        for i in range(nRows):
            print(labels[i] + "|" + ''.join(("%s" % x) for x in boardMask[i]) + "|")

        print(f"Current Score:{score:03} Last Move: ", end= "")
        print(f"[{coord[0]},{coord[1]}] is an INVALID COORDINATE")

        lastMove = f"[{coord[0]},{coord[1]}] is an INVALID COORDINATE"
        return boardData, boardMask, score, lastMove
# end def

def main( ) :
   r,c = 16,29
   iCoords = ["11", "1O", "G1", "GM", "77"]
   ships = ["[CARRIER=>", "[FRG=>", "[BCRUSR=>", "[DSTYR=>", "[SUBM=>"]
   score = 0
   lastMove = ""
   #                       carrier      frigate     submarine   cruiser             destroyer
   #           false miss  hit   false  hit   miss  hit   miss  hit    false  miss  hit   miss
   pCoords = ["AZ", "37", "1A", "CXA", "1O", "99", "79", "AP", "G2",  "  ",  "5K", "GO",  "2B"]

   gBoard = generateGameBoard(r, c)

   gMask = copy.deepcopy(gBoard)

   for i in range(len(iCoords)) :
      gBoard = loadShip(gBoard, r, c, iCoords[i], ships[i])
   for j in pCoords :
      print(checkCoord(r, c, j))

   for j in pCoords :
      print( )
      (gBoard, gMask, score, lastMove) = updateGameBoard(gBoard, gMask, r, c, j, score, lastMove)

if __name__ == "__main__" :
   main( )