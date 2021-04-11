import datetime, sys

from google.cloud import automl_v1
from flask import Flask, render_template
from google.api_core.client_options import ClientOptions

def inline_text_payload(file_path):
  with open(file_path, 'rb') as ff:
    content = ff.read()
  return {'text_snippet': {'content': content, 'mime_type': 'text/plain'} }


def get_prediction(file_path, model_name):
  options = ClientOptions(api_endpoint='eu-automl.googleapis.com')
  prediction_client = automl_v1.PredictionServiceClient(client_options=options)

  payload = {'text_snippet': {'content': "Aime les chats", 'mime_type': 'text/plain'} }
  # Uncomment the following line (and comment the above line) if want to predict on PDFs.
  # payload = pdf_payload(file_path)

  params = {}
  request = automl_v1.PredictRequest(name=model_name, payload=payload, params=params)
  response = prediction_client.predict(request)
  return response  # waits until request is returned



# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

@app.route('/evaluate', methods = ['POST'])
def evaluate():
    sentence = request.form['phrase']
    print(phrase)
    return redirect ('/index')

@app.route('/')
def root():
    return render_template('index.html')

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.

    app.run(host='127.0.0.1', port=8080, debug=True)
