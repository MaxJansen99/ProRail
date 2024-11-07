from flask import render_template, redirect, url_for, flash
from app import app, db
from models import User
from forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/register", methods=["GET", "POST"])
def register():
  if current_user.is_authenticated:
    return redirect(url_for("report"))
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
    flash("Uw account is aangemaakt!", "success")
    return redirect(url_for("login"))
  return render_template("register.html", form=form)

@app.route("/", methods=["GET", "POST"])
def login():
  if current_user.is_authenticated:
    return redirect(url_for("report"))
  form = LoginForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and user.check_password(form.password.data):
      login_user(user)
      return redirect(url_for("report"))
    else:
      flash("Login Onsuccesvol! Email en wachtwoord combinatie onjuist", "danger")
  return render_template("login.html", form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/report')
@login_required
def report():
  return render_template('report.html')

@app.route('/old')
@login_required
def old():
  return render_template('old.html')