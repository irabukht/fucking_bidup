from flask import Blueprint, session, redirect, url_for, render_template

main_bp = Blueprint("main_bp", __name__, template_folder="templates")

@main_bp.route("/")
def home():
    return render_template("home.html")

@main_bp.route("/dashboard")
def dashboard():
    # Protect the dashboard route
    if not session.get("user_id"):
        return redirect(url_for("auth_bp.login"))
    return render_template("dashboard.html", email=session.get("email"))
