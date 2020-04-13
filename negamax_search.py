#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 22:19:21 2020

@author: v1per
"""


""" almost the same as MiniMax, just implemented a little nicer """
""" chess is a zero sum game, therefore, one players gain is the other players loss """


import numpy as np
import chess
import chess.svg

from evaluate_board import evaluate_board
from minimax_search import quiescence
from IPython.display import SVG, display


def negamax(board, depth, alpha, beta):
    
    if depth == 0:
        return quiescence(board, alpha, beta)
    
    bestvalue = -np.inf
    
    for move in board.legal_moves:
        
        if move == chess.Move.null():
            continue
        
        board.push(move)
        score = -negamax(board, depth-1, -beta, -alpha)
        board.pop()
        
        if score >= beta:
            return score
        if score > alpha:
            alpha = score
        
        bestvalue = max(bestvalue, score)
        
    return bestvalue

def negamax_move(board, depth):
    
    bestmove = chess.Move.null()
    bestvalue = -np.inf
    alpha = -np.inf
    beta = np.inf
    
    for move in board.legal_moves:
        
        board.push(move)
        movevalue = -negamax(board, depth-1, -beta, -alpha)
        
        if bestvalue < movevalue:
            bestvalue = movevalue
            bestmove = move
        
        if movevalue > alpha:
            alpha = movevalue
        
        board.pop()
    
    return bestmove, movevalue


if __name__ == "__main__":
    board = chess.Board()
    
    bestvalue = negamax(board, 4, -np.inf, np.inf)
    print(bestvalue)
    
    bestmove, value = negamax_move(board, 4)
    
    print(bestmove, value)
    display(chess.svg.board(board=board,size=400))
    
