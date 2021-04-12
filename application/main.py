import datetime, sys
import os
from google.cloud import automl_v1, automl
from flask import Flask, request, render_template, jsonify
from google.api_core.client_options import ClientOptions

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='bsakey.json'
client_options = {'api_endpoint': 'eu-automl.googleapis.com:443'}

project_id = '1033040566143'
model_id = 'TCN4988515041545289728'
prediction_client = automl.PredictionServiceClient(client_options=client_options)
model_full_id = automl.AutoMlClient.model_path(project_id, "eu", model_id)

def predict(content):
  text_snippet = automl.TextSnippet(content=content, mime_type= "text/plain")
  payload = automl.ExamplePayload(text_snippet=text_snippet)
  response = prediction_client.predict(name=model_full_id, payload=payload)
  return response


app = Flask(__name__)

@app.route('/index/')
def index():
	return render_template('index.html')

@app.route('/evaluate', methods = ['GET', 'POST'])
def evaluate():
    phrase = ''
    if request.method == "POST":
        phrase = request.form.get('phrase')
        if phrase != '':
            niveau = predict(phrase)
            top_score = niveau.payload[0].classification.score
            level = niveau.payload[0].display_name
            phrase = level
            
    return render_template('index.html', phrase = phrase)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.

    app.run(host='127.0.0.1', port=8080, debug=True)
