#!/usr/bin/env python3
from flask import Flask
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route("/")
def helloWorld():
    return {'msg':'Hello World!'}

@app.route("/alive")
def alive():
    return {'alive':'true'}

@app.route("/time")
def givetime():
    return {'time':datetime.utcnow()}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)