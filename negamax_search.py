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
import chess.polyglot
import timeit
import time

from evaluate_board import evaluate_board
from minimax_search import quiescence
from minimax_search import minimax_move
from IPython.display import SVG, display


def negamax(board, depth, alpha, beta):
    
    if depth == 0:
        return quiescence(board, alpha, beta)
    
    bestvalue = -np.inf
    movelist = []
    
    for move in board.legal_moves:
        
        if board.is_capture(move):
            movelist.insert(0, move)
        else:
            movelist.append(move)
    
    for move in movelist:
        
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
    
    movelist = []
    
    for move in board.legal_moves:
        
        if board.is_capture(move):
            movelist.insert(0, move)
        else:
            movelist.append(move)
    
    for move in movelist:
        
        board.push(move)
        movevalue = -negamax(board, depth-1, -beta, -alpha)
        
        if bestvalue < movevalue:
            bestvalue = movevalue
            bestmove = move
        
        if movevalue > alpha:
            alpha = movevalue
        
        board.pop()
    
    return bestmove, bestvalue


def find_bestmove(board, depth, algo='negamax'):
    
    try:
        move = chess.polyglot.MemoryMappedReader(r"static/img/komodo.bin").weighted_choice(board)
        return move[4]
    
    except:
        
        if algo == 'negamax':
            move, value = negamax_move(board, depth)
            return move
        
        elif algo == 'minimax':
            move, value = minimax_move(board, depth)
            return move
        
        


if __name__ == "__main__":
    
    board0 = chess.Board()
    board1 = chess.Board('r1bqkbnr/pppp1ppp/2n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R')
    
    
    start = time.time()
    negamove, negavalue = negamax_move(board0, 4)
    end = time.time()
    negamax_time = end - start
    
    start = time.time()
    minimove, minivalue = minimax_move(board0, 4)
    end = time.time()
    minimax_time = end - start
    
    start = time.time()
    bestmove = find_bestmove(board0, 4)
    end = time.time()
    bestmove_time = end - start
    
    board0.push(bestmove)
    
    print("Negamax took %s seconds, returned: " % (negamax_time))
    print(negamove, negavalue)
    print()
    print("Minimax took %s seconds, returned: " % (minimax_time))
    print(minimove, minivalue)
    print()
    print("Bestmove-function took %s seconds, returned: " % (bestmove_time))
    print(bestmove)
    display(chess.svg.board(board=board0,size=400))
    
