#!./venv/bin/python3
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_render_template]

# FLASK_APP=main.py MAIL_USERNAME=holbietextme@gmail.com MAIL_PASSWORD=ryuichiiscool python main.py
import datetime

from flask import flash, Flask, redirect, render_template, request, url_for

from flask_mail import Mail, Message

from os import getenv
from threading import Thread

app = Flask(__name__)
app.url_map.strict_slashes = False

# app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'hard to guess string'  # might not need
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = getenv('MAIL_PASSWORD')
app.config['MAIL_SENDER'] = getenv('MAIL_USERNAME')
app.config['SSL_REDIRECT'] = False

mail = Mail(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if False:
            flash("This is a flashed message.")
        return redirect(url_for('index'))
    else:
        # For the sake of example, use static information to inflate the template.
        # This will be replaced with real information in later steps.
        dummy_times = [datetime.datetime(2018, 1, 1, 10, 0, 0),
                       datetime.datetime(2018, 1, 2, 10, 30, 0),
                       datetime.datetime(2018, 1, 3, 11, 0, 0),
                       ]

    return render_template('index.html', times=dummy_times)


def send_email_async(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject):  # , template, **kwargs):
    msg = Message(subject, sender=app.config['MAIL_SENDER'], recipients=[to])
    # render_template(template + '.txt', **kwargs)
    msg.body = 'this is the body'
    # render_template(template + '.html', **kwargs)
    msg.html = '<h1>header html</h1>'
    thr = Thread(target=send_email_async, args=[app, msg])
    thr.start()
    return thr


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [START gae_python37_render_template]
