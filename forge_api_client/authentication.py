from .utils import post_request

class Authentication:

    def authClientTwoLegged(self, client_id, client_secret, grant_type='client_credentials', scope='data:read'):

        url = 'https://developer.api.autodesk.com/authentication/v1/authenticate'
        data = {
            'client_id': client_id,
            'client_secret': client_secret,
            'grant_type': grant_type,
            'scope': scope
        }

        json_object = post_request(url, data)
        self.access_token = json_object['access_token']
        self.token_type = json_object['token_type']
        self.scope = scope
