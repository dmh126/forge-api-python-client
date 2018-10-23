from .utils import get_request, post_request, patch_request

class Versions:

    def getVersion(self, project_id, version_id):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/versions/%s' % (project_id, version_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    def getVersionDownloadFormats(self, project_id, version_id):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/versions/%s/downloadFormats' % (project_id, version_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    def getVersionDownloads(self, project_id, version_id):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/versions/%s/downloads' % (project_id, version_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    def getVersionItem(self, project_id, version_id):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/versions/%s/item' % (project_id, version_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    def getVersionRefs(self, project_id, version_id):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/versions/%s/refs' % (project_id, version_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    def getVersionLinks(self, project_id, version_id):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/versions/%s/links' % (project_id, version_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    def getVersionRelationshipsRefs(self, project_id, version_id):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/versions/%s/relationships/refs' % (project_id, version_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    def patchVersion(self, project_id, version_id, body):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/versions/%s' % (project_id, version_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
            'Content-Type': 'application/vnd.api+json'
        }

        data = body

        return patch_request(url, data, headers)

    def postVersion(self, project_id, body):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/versions' % (project_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
            'Content-Type': 'application/vnd.api+json'
        }

        data = body

        return post_request(url, data, headers)

    def postVersionRelationshipsRefs(self, project_id, version_id, body):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/versions/%s/relationships/refs' % (project_id, version_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
            'Content-Type': 'application/vnd.api+json'
        }

        data = body

        return post_request(url, data, headers)
