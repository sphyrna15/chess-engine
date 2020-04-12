# -*- coding: utf-8 -*-
"""
Evaluation funciton for python-chess board 

source : https://www.chessprogramming.org/Simplified_Evaluation_Function

Author @v1per
"""

import chess
import chess.svg
import numpy as np

from IPython.display import SVG, display




pawnstable = np.array([ 0,  0,  0,  0,  0,  0,  0,  0,
                       50, 50, 50, 50, 50, 50, 50, 50,
                       10, 10, 20, 30, 30, 20, 10, 10,
                       5,  5, 10, 25, 25, 10,  5,  5,
                       0,  0,  0, 20, 20,  0,  0,  0,
                       5, -5,-10,  0,  0,-10, -5,  5,
                       5, 10, 10,-20,-20, 10, 10,  5,
                       0,  0,  0,  0,  0,  0,  0,  0])

knightstable = np.array([-50,-40,-30,-30,-30,-30,-40,-50,
                         -40,-20,  0,  0,  0,  0,-20,-40,
                         -30,  0, 10, 15, 15, 10,  0,-30,
                         -30,  5, 15, 20, 20, 15,  5,-30,
                         -30,  0, 15, 20, 20, 15,  0,-30,
                         -30,  5, 10, 15, 15, 10,  5,-30,
                         -40,-20,  0,  5,  5,  0,-20,-40,
                         -50,-40,-30,-30,-30,-30,-40,-50])

bishopstable = np.array([-20,-10,-10,-10,-10,-10,-10,-20,
                         -10,  0,  0,  0,  0,  0,  0,-10,
                         -10,  0,  5, 10, 10,  5,  0,-10,
                         -10,  5,  5, 10, 10,  5,  5,-10,
                         -10,  0, 10, 10, 10, 10,  0,-10,
                         -10, 10, 10, 10, 10, 10, 10,-10,
                         -10,  5,  0,  0,  0,  0,  5,-10,
                         -20,-10,-10,-10,-10,-10,-10,-20])

rookstable = np.array([0,  0,  0,  0,  0,  0,  0,  0,
                       5, 10, 10, 10, 10, 10, 10,  5,
                       -5,  0,  0,  0,  0,  0,  0, -5,
                       -5,  0,  0,  0,  0,  0,  0, -5,
                       -5,  0,  0,  0,  0,  0,  0, -5,
                       -5,  0,  0,  0,  0,  0,  0, -5,
                       -5,  0,  0,  0,  0,  0,  0, -5,
                       0,  0,  0,  5,  5,  0,  0,  0])

queenstable = np.array([-20,-10,-10, -5, -5,-10,-10,-20,
                        -10,  0,  0,  0,  0,  0,  0,-10,
                        -10,  0,  5,  5,  5,  5,  0,-10,
                        -5,  0,  5,  5,  5,  5,  0, -5,
                        0,  0,  5,  5,  5,  5,  0, -5,
                        -10,  5,  5,  5,  5,  5,  0,-10,
                        -10,  0,  5,  0,  0,  0,  0,-10,
                        -20,-10,-10, -5, -5,-10,-10,-20])

mid_kingstable = np.array([-30,-40,-40,-50,-50,-40,-40,-30,
                           -30,-40,-40,-50,-50,-40,-40,-30,
                           -30,-40,-40,-50,-50,-40,-40,-30,
                           -30,-40,-40,-50,-50,-40,-40,-30,
                           -20,-30,-30,-40,-40,-30,-30,-20,
                           -10,-20,-20,-20,-20,-20,-20,-10,
                           20, 20,  0,  0,  0,  0, 20, 20,
                           20, 30, 10,  0,  0, 10, 30, 20])

end_kingstable = np.array([-50,-40,-30,-20,-20,-30,-40,-50,
                           -30,-20,-10,  0,  0,-10,-20,-30,
                           -30,-10, 20, 30, 30, 20,-10,-30,
                           -30,-10, 30, 40, 40, 30,-10,-30,
                           -30,-10, 30, 40, 40, 30,-10,-30,
                           -30,-10, 20, 30, 30, 20,-10,-30,
                           -30,-30,  0,  0,  0,  0,-30,-30,
                           -50,-30,-30,-30,-30,-30,-30,-50])



def evaluate_board(board, gamestat = "middle"):
    """ returns current board value
    
        Parameters
        ----------
        board : python-chess object with board
        gamestat : 'middle' or 'end' game?
        """
    
    if board.is_checkmate():
        if board.turn:
            return -9999
        else:
            return 9999
    
    if board.is_stalemate():
        return 0
    if board.is_insufficient_material():
        return 0
    
    wp = board.pieces(chess.PAWN, chess.WHITE)
    bp = board.pieces(chess.PAWN, chess.BLACK)
    wn = board.pieces(chess.KNIGHT, chess.WHITE)
    bn = board.pieces(chess.KNIGHT, chess.BLACK)
    wb = board.pieces(chess.BISHOP, chess.WHITE)
    bb = board.pieces(chess.BISHOP, chess.BLACK)
    wr = board.pieces(chess.ROOK, chess.WHITE)
    br = board.pieces(chess.ROOK, chess.BLACK)
    wq = board.pieces(chess.QUEEN, chess.WHITE)
    bq = board.pieces(chess.QUEEN, chess.BLACK)
    wk = board.pieces(chess.KING, chess.WHITE)
    bk = board.pieces(chess.KING, chess.BLACK)
    
    material_value = 100*(len(wp)-len(bp)) + 320*(len(wn)-len(bn)) + 330*(len(wb)-len(bb)) 
    material_value += 500*(len(wr)-len(br)) + 900*(len(wq)-len(bq))
    
    pawnsvalue = sum([pawnstable[chess.square_mirror(i)] for i in wp])
    pawnsvalue -= sum([pawnstable[i] for i in bp])
    
    knightsvalue = sum([knightstable[chess.square_mirror(i)] for i in wn])
    knightsvalue -= sum([knightstable[i] for i in bn])
    
    bishopsvalue = sum([bishopstable[chess.square_mirror(i)] for i in wb])
    bishopsvalue -= sum([bishopstable[i] for i in bb])
    
    rooksvalue = sum([rookstable[chess.square_mirror(i)] for i in wr])
    rooksvalue -= sum([rookstable[i] for i in br])
    
    queensvalue = sum([queenstable[chess.square_mirror(i)] for i in wq])
    queensvalue -= sum([queenstable[i] for i in bq])
    
    if gamestat == "middle":
        kingstable = mid_kingstable
    else:
        kingstable = end_kingstable
    
    kingsvalue = sum([kingstable[chess.square_mirror(i)] for i in wk])
    kingsvalue -= sum([kingstable[i] for i in bk])
    
    boardvalue = pawnsvalue + knightsvalue + bishopsvalue + rooksvalue + queensvalue + kingsvalue
    
    if board.turn:
        return boardvalue
    else:
        return -boardvalue
    
    
    



if __name__ == "__main__":
    
    board = chess.Board()
    display(SVG(chess.svg.board(board=board,size=400)))
    
    board.push_san("e4")
    board.push_san("e5")
    board.push_san("Nf3")
    board.push_san("Nf6")
    board.push_san("Ne5")
    
    display(SVG(chess.svg.board(board=board,size=400)))        
    print(evaluate_board(board))
    
    


