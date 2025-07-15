from flask import render_template, redirect, url_for, request, flash
from app import app, db
from models import User
from forms import RegistrationForm, LoginForm, PredictForm
from flask_login import login_user, current_user, logout_user, login_required
from predictor import Predictor


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("report"))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            email=form.email.data,
        )

        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        flash("Uw account is aangemaakt! U kunt nu inloggen.", "success")

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
            flash(
                "Login niet succesvol! Email en wachtwoord combinatie onjuist.",
                "danger",
            )

    return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()

    return redirect(url_for("login"))


@app.route("/report", methods=["GET", "POST"])
@login_required
def report():
    if request.method == "POST":
        data = {
            "stm_sap_melddatum": request.form.get("stm_sap_melddatum"),
            "stm_sap_meldtijd": request.form.get("stm_sap_meldtijd"),
            "stm_aanntpl_tijd": request.form.get("stm_aanntpl_tijd"),
            "stm_progfh_in_duur": int(request.form.get("stm_progfh_in_duur")),
            "stm_prioriteit": int(request.form.get("stm_prioriteit")),
            "stm_oorz_code": int(request.form.get("stm_oorz_code")),
            "stm_contractgeb_mld": int(request.form.get("stm_contractgeb_mld")),
            "stm_techn_mld_encoded": int(request.form.get("stm_techn_mld_encoded")),
        }

        predictor = Predictor()  # Instantiate the Predictor class
        _, prediction = predictor.predict(data)  # Pass data as it is

        return render_template("prediction.html", prediction=prediction)

    form = PredictForm()

    return render_template("report.html", form=form)


@app.route("/old")
@login_required
def old():
    return render_template("old.html")