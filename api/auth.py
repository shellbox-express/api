from requests.auth import HTTPBasicAuth
from requests import post 

class Auth:
    def __init__(self, client_id, client_secret, base_url="https://api-hackaraizen.sensedia.com/oauth/"):
    	self.auth = HTTPBasicAuth(client_id, client_secret)
    	self.base_url = base_url
    def token(self):
    	body = {
    		"grant_type": "client_credentials"
    	}
    	r = post(self.base_url + "access-token", json=body, auth=self.auth)
    	r.raise_for_status()
    	return r.json()
    	