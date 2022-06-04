from asyncio.log import logger
import email
from unittest import TestCase

from flask import request, Flask

from app import db, app
from app.models import User
from app.services import google_auth_service
from tests import logger


class TestLoginRoutes(TestCase):
    """
    Test the routes for login
    """

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.user = User(name='test', email="email", profile_pic="pic")

    def test_login_route(self):
        google_provider_cfg = google_auth_service.get_provider_cfg()
        authorization_endpoint = google_provider_cfg["authorization_endpoint"]

        # Use library to construct the request for Google login and provide
        # scopes that let you retrieve user's profile from Google
        with app.test_request_context():
            request_uri = google_auth_service.client.prepare_request_uri(
                authorization_endpoint,
                redirect_uri=request.base_url + "/callback",
                scope=["openid", "email", "profile"],
            )

            logger.debug(request_uri)
