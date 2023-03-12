from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


@app.route('/')
def func1():
    return "This is Maintenance Accounting site"


@app.route('/sites')
def sites():
    return "here must be a list of sites"


@app.route('/visits')
def visits():
    return "here must be a visits list"


if __name__ == '__main__':
    app.run()
