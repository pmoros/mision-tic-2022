from asyncio.log import logger
from unittest import TestCase
import app.services as services
from tests import logger


class TestGoogleAuth(TestCase):
    def setUp(self):
        self.auth_service = services.google_auth_service

    def test_get_google_provider_cfg(self):
        provided_cfg = self.auth_service.get_provider_cfg()
        logger.debug(provided_cfg)
        assert provided_cfg.get('authorization_endpoint') is not None

    def test_get_authorization_endpoint(self):
        provided_endpoint = self.auth_service.get_authorization_endpoint()
        logger.debug(provided_endpoint)
        assert provided_endpoint is not None

    def test_verify_valid_email(self):
        user_info = {
            'email': None}
        assert self.auth_service.verify_valid_email(user_info) is not None
