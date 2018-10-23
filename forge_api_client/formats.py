from .utils import get_request

class Formats:

    def getFormats(self):

        url = 'https://developer.api.autodesk.com/modelderivative/v2/designdata/formats'

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)
