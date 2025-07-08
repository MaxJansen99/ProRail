from flask import render_template, redirect, url_for, request, flash
from app import app, db
from models import User
from forms import RegistrationForm, LoginForm, PredictForm
from flask_login import login_user, current_user, logout_user, login_required
import pandas as pd
import numpy as np


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


@app.route("/report")
@login_required
def report():
    form = PredictForm()

    return render_template("report.html", form=form)


@app.route("/old")
@login_required
def old():
    df = pd.read_csv("static/data/data.csv")
    df = df[
        [
            "stm_oorz_code",
            "stm_sap_melddatum",
            "stm_sap_meldtijd",
            "stm_geo_mld",
            "stm_aanntpl_dd",
            "stm_aanntpl_tijd",
            "stm_fh_dd",
            "stm_fh_tijd",
            "stm_techn_mld",
            "stm_prioriteit",
            "stm_fh_duur",
        ]
    ]
    df = df.rename(
        columns={
            "stm_oorz_code": "Oorzaakcode",
            "stm_sap_melddatum": "Melddatum",
            "stm_sap_meldtijd": "Meldtijd",
            "stm_geo_mld": "Geocode",
            "stm_aanntpl_dd": "Aannemer Aanwezig Datum",
            "stm_aanntpl_tijd": "Aannemer Aanwezig Tijd",
            "stm_fh_dd": "Hersteldatum",
            "stm_fh_tijd": "Hersteltijd",
            "stm_techn_mld": "Technischemelding",
            "stm_prioriteit": "Prioriteit",
            "stm_fh_duur": "Herstelduur",
        }
    )

    pages = int(np.ceil(len(df) / 22))
    current = int(request.args.get("page", 1))
    start = (current - 1) * 22
    end = current * 22
    data = df[start:end].to_dict(orient="records")

    return render_template(
        "old.html", data=data, current=current, start=start, end=end, pages=pages
    )

