import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
from models.user import User



app = Flask(__name__)

from app import views

#
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)




@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', user=admin)



@app.route('/blog')
def blog():
    pass

    
    
    

    
