# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 21:10:13 2022

@author: Usuario
"""
import flask
from flask import request,redirect

app=flask.Flask(__name__)


import youtube_dl
@app.route('/',methods=['GET'])
def home():
    return redirect("http://www.example.com", code=302)
