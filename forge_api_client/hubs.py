from .utils import get_request, authorized

class Hubs:

    @authorized
    def getHubs(self):

        url = 'https://developer.api.autodesk.com/project/v1/hubs'

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    @authorized
    def getHub(self, hub_id):

        url = 'https://developer.api.autodesk.com/project/v1/hubs/%s' % hub_id

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)
