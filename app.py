from flask import Flask, render_template
import json
import os
import random
import requests

GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']
MAX_RESULTS = 50
QUERIES = [
    ' minutes workout',
    ' minutes yoga',
    ' minutes pilates',
    ' minutes stretching',
    ' minutes hiit',
    ' minutes tai chi',
    ' minutes qi gong',
]


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='iMhgQ7V0e2Co7mcDlyiebe7mVPDsRlg0',
    )

    return app


app = create_app()


@app.route('/')
def index():
    video_id = random_youtube_video(duration=20)
    return render_template('video.html', video_id=video_id)


def random_youtube_video(duration):
    query = random_query(duration=20)
    result = search_youtube(query)
    index = random.randint(0, len(result['items']) - 1)

    return result['items'][index]['id']['videoId']


def random_query(duration):
    index = random.randint(0, len(QUERIES))
    return '{} {}'.format(duration, QUERIES[index])


def search_youtube(query):
    url = 'https://www.googleapis.com/youtube/v3/search?q={query}&type=video&part=snippet&key={api_key}&maxResults={max_results}&order=rating'.format(
            query=query,
            api_key=GOOGLE_API_KEY,
            max_results=MAX_RESULTS)
    response = requests.get(url)
    return response.json()
