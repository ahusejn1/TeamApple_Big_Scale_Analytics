
import datetime, sys
import os
import google
from google.cloud import automl_v1, automl
import flask
from flask import Flask, request, render_template, jsonify
from google.api_core.client_options import ClientOptions

app = Flask(__name__)

def predict(input, model_name):
  options = ClientOptions(api_endpoint='eu-automl.googleapis.com')
  prediction_client = automl_v1.PredictionServiceClient(client_options=options)

  payload = {'text_snippet': {'content': input, 'mime_type': 'text/plain'} }
  params = {}
  automl_request = automl_v1.PredictRequest(name=model_name, payload=payload, params=params)
  automl_response = prediction_client.predict(automl_request)
  return automl_response



@app.route('/', methods = ['GET', 'POST'])
def root():
    form_data = ''
    difficulty = ''
    result =''
    if request.method == "POST":
        form_data = request.form.get('textinput')
        difficulty = predict(form_data, 'projects/1033040566143/locations/eu/models/TCN1026037862761496576').payload[0].display_name
        result = difficulty
    return render_template('index.html', result = result, text=form_data)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.

    app.run(host='127.0.0.1', port=8080, debug=True)
