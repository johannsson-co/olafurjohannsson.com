from flask.ext.wtf import Form

from wtforms import StringField, BooleanField, TextField, PasswordField, validators
from wtforms.validators import DataRequired

class LoginForm(Form):
    username = TextField('Username', [validators.Required()])
    password = PasswordField('Password', [validators.Required()])
    remember_me = BooleanField('remember_me', default=False)