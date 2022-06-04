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
GOOGLE_AUTH_ENDPOINT = "https://www.googleapis.com/oauth2/v4/token"


class GoogleAuthService():
    def __init__(self, client, discovery_url, authorization_endpoint):
        self.client = client
        self.discovery_url = discovery_url
        self.authorization_endpoint = authorization_endpoint

    def get_provider_cfg(self):
        return requests.get(self.discovery_url).json()

    def get_authorization_endpoint(self):
        return self.authorization_endpoint

    def get_authorized_token(self, code, url, base_url):
        google_provider_cfg = self.get_provider_cfg()
        authorization_endpoint = self.get_authorization_endpoint()

        # Prepare and send a request to get tokens! Yay tokens!
        token_url, headers, body = self.client.prepare_token_request(
            authorization_endpoint,
            authorization_response=url,
            redirect_url=base_url,
            response_type="code",
            code=code
        )

        token_response = requests.post(
            token_url,
            headers=headers,
            data=body,
            auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
        )

        return token_response


google_auth_service = GoogleAuthService(
    google_app_client, GOOGLE_DISCOVERY_URL, GOOGLE_AUTH_ENDPOINT)
