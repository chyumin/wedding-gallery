from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class CreateUserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    name = StringField('Name')
    password = PasswordField('Password', validators=[DataRequired()])
    master = BooleanField('Master')
    submit = SubmitField('Create User')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
