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
import datetime
from flask import Flask, render_template
from flask_cors import CORS
from google.cloud import datastore


app = Flask(__name__)
storage = datastore.Client()

def store_time(dt):
    entity = datastore.Entity(key=storage.key('visit'))
    entity.update({
        'timestamp': dt
    })

    storage.put(entity)


def fetch_times(limit):
    query = storage.query(kind='visit')
    query.order = ['-timestamp']

    times = query.fetch(limit=limit)

    return times

@app.route('/')
def root():
    # Store the current access time in Datastore.
    store_time(datetime.datetime.now())

    # Fetch the most recent 10 access times from Datastore.
    times = fetch_times(10)

    return render_template('index.html', times=times)

@app.route('/api/user', methods=['POST'])
def api_user(data):
    pass
    # data = []
    # error = None
    # select = request.form.get('comp_select')
    # resp = query_api(select)
    # pp(resp)
    # if resp:
    #     data.append(resp)
    # if len(data) != 2:
    #     error = 'Bad Response from Weather API'
    # return request.Response() ('result.html', data=data, error=error)


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
