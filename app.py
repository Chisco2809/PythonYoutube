# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 21:10:13 2022

@author: Usuario
"""
import flask
from flask import request

app=flask.Flask(__name__)


import youtube_dl
@app.route('/',methods=['GET'])
def home():
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})
    videoid=request.args['VideoID']
    with ydl:
        result = ydl.extract_info('https://www.youtube.com/watch?v='+videoid,download=False   )

        if 'entries' in result:
            # Can be a playlist or a list of videos
            video = result['entries'][0]
        else:
    # Just a video
            video = result
    
    video_url = result['formats'][0]['url']

    return video_url
