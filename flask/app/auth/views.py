from flask import render_template, redirect, flash, current_app, url_for
from flask_login import logout_user, login_required, login_user

from . import auth
from .forms import LoginForm
from ..models.user import User
from ..utils.routing import get_next_page


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.email == form.email.data).first()
        if user is not None and user.verify_password(password=form.password.data):
            login_user(user)
            return redirect(get_next_page())
        # Invalid login
        flash("Invalid credentials", "dark")

    return render_template("auth/login.html", form=form)


@auth.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    flash("You have been logged out", "info")
    return redirect(url_for("auth.login"))
