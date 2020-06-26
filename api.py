import flask
from flask import jsonify
from functions import return_users_near_london

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home(): 
    return jsonify(return_users_near_london())

app.run()
