from flask import Flask
from flask_cors import CORS
import json

from .routes import rest_api
from .models import db

app = Flask(__name__)

app.config.from_object('api.config.BaseConfig')

db.init_app(app)
rest_api.init_app(app)
CORS(app)


# Custom responses

@app.after_request
def after_request(response):
    if int(response.status_code) >= 400:
        response_data = json.loads(response.get_data())
        if 'errors' in response_data:
            response_data = {'success': False,
                             'msg': list(response_data['errors'].items())[0][1]}
            response.set_data(json.dumps(response_data))
        response.headers.add('Content-Type', 'application/json')
    return response