# Standard libraries imports
import os

# Standard libraries imports
import requests
# Third party libraries imports
from dotenv import load_dotenv
from oauthlib.oauth2 import WebApplicationClient

load_dotenv()

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

google_app_client = WebApplicationClient(GOOGLE_CLIENT_ID)


class GoogleAuthService():
    def __init__(self, client, discovery_url):
        self.client = client
        self.discovery_url = discovery_url

    def get_provider_cfg(self):
        return requests.get(self.discovery_url).json()


google_auth_service = GoogleAuthService(
    google_app_client, GOOGLE_DISCOVERY_URL)
