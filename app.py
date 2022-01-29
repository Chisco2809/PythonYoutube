# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 21:10:13 2022

@author: Usuario
"""
import flask
from flask import request

app=flask.Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return 'Hello word'
