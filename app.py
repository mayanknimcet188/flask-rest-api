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
#Article Model
class Article(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(64))
    title = db.Column(db.String(100),unique=True)
    content = db.Column(db.Text)

    def __init__(self,author,title,content):
        self.author = author
        self.title = title
        self.content = content

    def __repr__(self):
        return '< Article %r >' % self.title

#Creating the article schema using marshmallow
class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id','author','title','content')

#Initializing the schema
#For a single article
article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)

#Run the flask server
if __name__ == '__main__':
    app.run(debug=True)


