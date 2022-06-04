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
