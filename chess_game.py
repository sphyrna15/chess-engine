#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 10:12:39 2020

@author: v1per
"""

from flask import Flask, request, render_template, redirect
import chess
import chess.svg
import time

from IPython.display import SVG, display
from negamax_search import negamax_move

app = Flask(__name__)
board = chess.Board()
board.reset()

""" data variables """

data0 =  {
        'fen' : 'start',
        'status' : 'Please make a move: ',
        'move' : '',
        'engine_move' : ''
    }
data =  {
        'fen' : 'start',
        'status' : 'Please make a move: ',
        'move' : '',
        'engine_move' : ''
    }



""" Flask Application """

@app.route("/")
def index():
    return render_template('home.html',)

board = chess.Board()

@app.route("/chessgame")
def chessgame():
    return render_template('chessgame.html', data = data)


@app.route("/chessgame", methods = ["POST"])
def get_move():

    move = request.form['move']
    depth = 4
    
    if len(move) < 4 or 5 < len(move):
        data['status'] = 'Input sequnce must have 4 or 5 characters, example: e2e4'
        return render_template('chessgame.html', data = data) 
    
    move = chess.Move.from_uci(move)

    if move not in board.legal_moves:
        data['status'] = "sorry, that is not a legal move in this position, try again..."
        return render_template('chessgame.html', data = data)
    
    board.push(move)
    fen_rep = board.fen()
    data['fen'] = fen_rep
    data['status'] = 'Please wait for the engine to make a move...'
    render_template('chessgame.html', data = data)

    bestmove, value = negamax_move(board, depth)
    board.push(bestmove)
    fen_rep = board.fen()
    data['fen'] = fen_rep
    data['status'] = 'It expects the boardvalue '+str(depth)+' moves into the future to be '+str(value) 
    data['engine_move'] = str(bestmove)

    return render_template('chessgame.html' , data = data)

@app.route('/stop_and_reset')
def stop():
    data['status'] = 'You can continue playing anytime, just make a move'
    data['fen'] = 'start'
    board.reset()
    return redirect('/chessgame')

@app.route('/undo_move')
def undo():
    board.pop()
    board.pop()
    fen = board.fen()
    data['fen'] = fen
    data['status'] = 'Last move successfully undone...'
    return redirect('/chessgame')



if __name__ == "__main__":
    app.run(debug = True)

