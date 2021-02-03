from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Initialize Flask app instance
app = Flask(__name__)

#HTTP Routes
@app.route('/', methods=['GET'])
def index():
    return jsonify({'message':'Hello world'})

#Run the flask server
if __name__ == '__main__':
    app.run(debug=True)


