from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, SubmitField
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

class PredictForm(FlaskForm):
  stm_oorz_code = IntegerField('Stm-Oorz-Code', validators=[DataRequired()])
  stm_geo_mld = IntegerField('Stm-Geo-MLD', validators=[DataRequired()])
  stm_sap_melddatum = IntegerField('Stm-Sap-Meld-Datum', validators=[DataRequired()])
  stm_aanntpl_tijd = IntegerField('Stm-Aantpl-Tijd', validators=[DataRequired()])
  stm_techn_mld = IntegerField('Stm-Techn-MLD', validators=[DataRequired()])
  stm_prioriteit = IntegerField('Stm-Prioriteit', validators=[DataRequired()])