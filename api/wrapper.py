import datetime

import requests

from .auth import Auth


class Wrapper:

    def __init__(self, client_id, client_secret, base_url):
        self.client_id = client_id
        self.auth = Auth(client_id, client_secret)
        self._acquire_token()

    def _acquire_token(self):
        self.token = self.auth.token()
        self.token_expires = datetime.datetime.now() + \
            datetime.timedelta(seconds=self.token["expires_in"])

    def call(self, endpoint, method="GET", headers=None, body=None):
        if self.token_expires > datetime.datetime.now():
            self._acquire_token()

        if not headers:
            headers = {}

        headers["access_token"] = self.token["access_token"]
        headers["client_id"] = self.client_id

        caller = getattr(requests, method.lower())

        return caller(endpoint, headers=headers)
