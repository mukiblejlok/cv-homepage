from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[Email(), DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
