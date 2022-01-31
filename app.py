# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 21:10:13 2022

@author: Usuario
"""
import flask
from flask import request,redirect
import webbrowser

app=flask.Flask(__name__)


import youtube_dl
@app.route('/',methods=['GET'])
def home():
    return redirect('https://www.youtube.com/watch?v=GjVa2o8-WnI&ab_channel=Music26Online')
