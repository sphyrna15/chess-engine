#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 20:24:29 2020

@author: v1per
"""


""" Implement MinMax Search Algorithm with AlphaBeta pruning in Python for chess """

import chess
import chess.svg
import numpy as np

from IPython.display import SVG, display
from evaluate_board import evaluate_board



""" Quiescence algorithm to avoid Horizon-Effect """
def quiescence(board, alpha, beta):
    board_val = evaluate_board(board)
    
    if board_val >= beta:
        return beta
    if alpha < board_val:
        alpha = board_val
    
    for move in board.legal_moves:
        
        if board.is_capture(move):
            
            board.push(move)
            score = -quiescence(board, alpha, beta)
            board.pop()
            
            if score >= beta:
                return beta
            if score > alpha:
                alpha = score
    
    return alpha

""" AlphaBeta pruning applied to MinMax search algorithm """ 

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
    
def find_bestmove(board, depth):
    bestmove = chess.Move.null()
    bestvalue = -np.inf
    alpha = -np.inf
    beta = np.inf
    
    for move in board.legal_moves:
        
        board.push(move)
        movevalue = AlphaBeta(board, depth-1, alpha, beta, maximizer=False)
        
        if bestvalue < movevalue:
            bestvalue = movevalue
            bestmove = move
        
        if movevalue > alpha:
            alpha = movevalue
        
        board.pop()
    
    return bestmove, movevalue
        


    
if __name__ == "__main__":
    board = chess.Board('rnbqkb1r/pppp1ppp/5n2/4N3/4P3/8/PPPP1PPP/RNBQKB1R b KQkq - 0 3')
    
    bestvalue = AlphaBeta(board, 4, -np.inf, np.inf, True)
    print(bestvalue)
    
    bestmove, value = find_bestmove(board, 4)
    
    print(bestmove, value)
    display(SVG(chess.svg.board(board=board,size=400)))
            
        
        
        



