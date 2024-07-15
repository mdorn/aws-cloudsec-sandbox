#!/usr/bin/env python
import os

from flask import Flask
from pymongo import MongoClient
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = MongoClient('mongodb://localhost/?timeoutMS=1000')

@app.route('/')
def todo():
    try:
        client.admin.command('ismaster')
    except:
        return 'Server not available'
    return 'Hello from the MongoDB client!\n'


@app.route('/hello')
def hello():
    return 'Hello world'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('FLASK_SERVER_PORT', 8080), debug=True)
    # TODO: production WSGI server
