#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 17:42:15 2020

@author: v1per
"""


""" script to play against various engines """

import numpy as np
import chess
import chess.svg

from IPython.display import display
from evaluate_board import evaluate_board
from minimax_search import minimax_move
from negamax_search import negamax_move


board = chess.Board()


print("your are playing white")
print("you can 'type stopgame' to stop the game at any time")
print()
display(chess.svg.board(board=board,size=400))
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
    if len(move) < 4 or 5 < len(move):
        print("input sequence must be of length 4 or 5, ex: e2e4")
        print()
        continue
    
    move = chess.Move.from_uci(move)
    
    if move not in board.legal_moves:
        print("sorry, that is not a legal move in this position, try again")
        continue
    
    board.push(move)
    display(chess.svg.board(board=board,size=400))
    
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
    
    print()
    print("the engine is working on it... ")
    engine_move, value = negamax_move(board, 3)
    print("the engine chose to resond with ")
    print()
    print(engine_move)
    print()    
    print("it expects the board value 3 steps into the future to be " + str(value))
    print()
    
    board.push(engine_move)
    if board.is_check():
        print("CHECK")
    
    display(chess.svg.board(board=board,size=400))
    
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
    
        
            
        
        
    
    
    
    
    
    
    
    
    
    


