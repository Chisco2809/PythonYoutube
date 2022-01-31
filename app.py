# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 21:10:13 2022

@author: Usuario
"""
import flask
from flask import request,redirect,Response
import requests
app=flask.Flask(__name__)


import youtube_dl
@app.route('/',methods=['GET'])
def home():
    r = requests.get("http://unoredradio.com:9768/;stream.mp3_", stream=True)
    return Response(stream_with_context(result.iter_content()),                 content_type = result.headers['Content-Type'])
    

