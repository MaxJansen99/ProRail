from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
  firstname = StringField('Voornaam', validators=[DataRequired(), Length(min=2, max=20)])
  lastname = StringField('Achternaam', validators=[DataRequired(), Length(min=2, max=20)])
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Wachtwoord', validators=[DataRequired()])
  confirm_password = PasswordField('Bevestig Wachtwoord', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Registreren')

class LoginForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Wachtwoord', validators=[DataRequired()])
  submit = SubmitField('Inloggen')
