import datetime, sys

from google.cloud import automl_v1
from flask import Flask, render_template, jsonify
from google.api_core.client_options import ClientOptions

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

@app.route('/index/')
def index():
	return render_template('index.html')

@app.route('/evaluate', methods = ['GET', 'POST'])
def evaluate():
	phrase = ''
    if request.method == "POST":
      phrase = request.form.get('phrase')
      niveau = predict.predict(phrase)
      top_score = niveau.payload[0].display_name
		return phrase = top_score

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.

    app.run(host='127.0.0.1', port=8080, debug=True)
