import logging
from logging.handlers import RotatingFileHandler
from urllib import response
from flask import jsonify, redirect, request, url_for
from flask_login import (
    current_user,
    login_required,
    login_user,
    logout_user,
)
import requests
from app import app, db
from app.models import User, load_test_data
from app.controllers import user_controller
from app.services import google_auth_service

# Set format that both loggers will use:
formatter = logging.Formatter(
    "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")

# Set logger A for known errors
log_handler = RotatingFileHandler(
    'app_debug.log', maxBytes=10000, backupCount=1)
log_handler.setFormatter(formatter)
log_handler.setLevel(logging.INFO)
a = logging.getLogger('app_debug')
a.addHandler(log_handler)


@app.route("/")
def index():
    if current_user.is_authenticated:
        return (
            "<p>Hello, {}! You're logged in! Email: {}</p>"
            "<div><p>Google Profile Picture:</p>"
            '<img src="{}" alt="Google profile pic"></img></div>'
            '<a class="button" href="/logout">Logout</a>'.format(
                current_user.name, current_user.email, current_user.profile_pic
            )
        )
    else:
        return '<a class="button" href="/login">Google Login</a>'


@app.route("/login")
def login():
    # Find out what URL to hit for Google login
    google_provider_cfg = google_auth_service.get_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = google_auth_service.client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )

    app.logger.info(request_uri)
    return redirect(request_uri)


@app.route("/login/callback")
def callback():
    """Authentication callback route, used by Google OAuth API to confirm login."""
    # # Get authorization code Google sent back to you
    code = request.args.get("code")

    user_token = google_auth_service.get_authorized_token(
        code, request.url, request.base_url)
    user_info = google_auth_service.get_user_info(user_token)

    if google_auth_service.verify_valid_email(user_info):
        user = user_controller.get_user(user_info)
    else:
        return "User email not available or not verified by Google.", 400

    if not user:
        user = user_controller.create_user(user_info)

    login_user(user)

    # Send user back to homepage
    return redirect(url_for("index"))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/create_database", methods=["POST"])
def create_database():
    db.create_all()
    return "Database created"


@app.route("/drop_database", methods=["POST"])
def drop_database():
    db.drop_all()
    return "Database dropped"


@app.route("/load_database_test_data", methods=["POST"])
def load_database_test_data():
    load_test_data()
    return "Database test data loaded"
