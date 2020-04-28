from flask import Flask, render_template, request
import logging
import os
import random
import requests

GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']
MAX_RESULTS = 50
QUERIES = [
    ' workout',
    ' yoga',
    ' pilates',
    ' stretching',
    ' hiit',
    ' tai chi',
    ' qi gong',
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
    duration = request.args.get('d', '20')
    print('duration', duration)
    video_id = random_youtube_video(duration=duration)
    return render_template('video.html', video_id=video_id)


def random_youtube_video(duration):
    query = random_query(duration=duration)

    app.logger.info('Youtube: Searching for »{}«'.format(query))

    result = search_youtube(query)

    app.logger.info('Youtube: Got {} results'.format(len(result['items'])))

    index = random.randint(0, len(result['items']) - 1)
    video_id = result['items'][index]['id']['videoId']

    app.logger.info('Youtube: Chose random video with id {}'.format(video_id))

    return video_id


def random_query(duration):
    index = random.randint(0, len(QUERIES) - 1)
    return '"{} minutes" {}'.format(duration, QUERIES[index])


def search_youtube(query):
    url = 'https://www.googleapis.com/youtube/v3/search?q={query}&type=video&part=snippet&key={api_key}&maxResults={max_results}&order=rating'.format(
            query=query,
            api_key=GOOGLE_API_KEY,
            max_results=MAX_RESULTS)
    response = requests.get(url)
    return response.json()


if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
