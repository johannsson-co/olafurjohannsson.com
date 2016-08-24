import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
from models.user import User

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)




@app.route('/')
def index():
    admin = User.query.filter_by(username='admin').first()
    print(admin)
    return render_template('index.html')



@app.route('/blog')
def blog():
    pass


if __name__ == '__main__':
    app.run(debug=True)
    db.create_all()

    admin = User('admin', 'olafurjohannss@gmail.com')
    db.session.add(admin)
    db.session.commit()
