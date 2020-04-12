#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 20:24:29 2020

@author: v1per
"""


""" Implement MinMax Search Algorithm in Python for chess """

import chess
import chess.svg
import numpy as np

from IPython.display import SVG, display
from evaluate_board import evaluate_board


def quiescence(board, alpha, beta):
    board_val = evaluate_board(board)
    return board_val



def AlphaBeta(board, depth, alpha, beta, maximizer = True):
    
    
    if depth == 0:
        return quiescence(board, alpha, beta)
    
    if maximizer:
        
        maxvalue = -np.inf
        
        for move in board.legal_moves:
            
            board.push(move)
            move_eval = AlphaBeta(board, depth-1, alpha, beta, False)
            board.pop()
            maxvalue = max(maxvalue, move_eval)
            alpha = max(maxvalue, alpha)
            
            if beta <= alpha:
                break
        
        return maxvalue

    else:
        
        minvalue = np.inf
        
        for move in board.legal_moves:
            
            board.push(move)
            move_eval = AlphaBeta(board, depth-1, alpha, beta, True)
            board.pop()
            minvalue = min(minvalue, move_eval)
            beta = min(minvalue, beta)
            
            if beta <= alpha:
                break
            
        return minvalue
    
def find_bestmove(board, alpha, beta, maximizer):
    return None


    
if __name__ == "__main__":
    board = chess.Board()
    
    bestvalue = AlphaBeta(board, 4, -np.inf, np.inf, True)
    print(bestvalue)
    display(SVG(chess.svg.board(board=board,size=400)))
            
        
        
        



