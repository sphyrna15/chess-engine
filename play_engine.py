#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 17:42:15 2020

@author: v1per
"""


""" script to play against various engines """

import numpy as np
import chess
import chess.svgp

from IPython.display import SVG, display
from evaluate_board import evaluate_board
from minmax_search import find_bestmove


board = chess.Board()


print("your are playing white")
print("you can 'type stopgame' to stop the game at any time")
display(SVG(chess.svg.board(board=board,size=400)))
game = True

while game:
    
    print("please choose your move or type 'undo' to undo your last move")
    move = input()
    
    if move == "undo":
        board.pop()
        board.pop()
        continue
    if move == "stopgame":
        break
    
    move = chess.Move.from_uci(move)
    
    if move not in board.legal_moves:
        print("sorry, that is not a legal move in this position, try again")
        continue
    
    board.push(move)
    display(SVG(chess.svg.board(board=board,size=400)))
    
    if board.is_game_over():
        print("the game is over")
        
        if board.is_stalemate():
            print("it is a stalemate")
        elif board.is_checkmate():
            print("CHECKMATE, YOU WIN!")
        elif board.is_insufficient_material():
            print("Insufficient Material to contiue the game")
        
        game = False
        break
    
    engine_move, value = find_bestmove(board, 3)
    print("the engine chose to resond with " + engine_move)
    print("it expects the board value after 3 steps to be " + value)
    
    board.push(engine_move)
    if board.is_check():
        print("CHECK")
    
    display(SVG(chess.svg.board(board=board,size=400)))
    
    if board.is_game_over():
        print("the game is over")
        
        if board.is_stalemate():
            print("it is a stalemate")
        elif board.is_checkmate():
            print("CHECKMATE, THE ENGINE WINs!")
        elif board.is_insufficient_material():
            print("Insufficient Material to contiue the game")
        
        game = False
        break
    
        
            
        
        
    
    
    
    
    
    
    
    
    
    


