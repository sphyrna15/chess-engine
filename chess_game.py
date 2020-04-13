#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 10:12:39 2020

@author: v1per
"""

from flask import Flask, request, render_template
import chess
import chess.svg

from IPython.display import SVG, display
import os

posts = [
    {
        'author' : 'Tim Launer',
        'title' : 'Blogpost 1',
        'content' : 'post content',
        'date_posted' : 'today'
    },
    {
        'author' : 'not Tim Launer',
        'title' : 'Blogpost 2',
        'content' : 'not the same post content',
        'date_posted' : 'not today'
    }
]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html',)

@app.route("/chessgame")
def chessgame():
    return render_template('chessgame.html')


if __name__ == "__main__":
    app.run(debug = True)


