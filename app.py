from flask import Flask, render_template
import os

GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='iMhgQ7V0e2Co7mcDlyiebe7mVPDsRlg0',
    )

    return app


app = create_app()


@app.route('/')
def index():
    return render_template('video.html', video_id='UItWltVZZmE')
