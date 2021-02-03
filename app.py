from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Initialize Flask app instance
app = Flask(__name__)
#Setting up the base directory
basedir = os.path.abspath(os.path.dirname(__file__))
#Database Setup
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Initialize DB
db = SQLAlchemy(app)
#Init masrhmallow
ma = Marshmallow(app)


#Run the flask server
if __name__ == '__main__':
    app.run(debug=True)


