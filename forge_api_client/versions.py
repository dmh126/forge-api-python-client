from .utils import get_request, post_request, patch_request, authorized

class Versions:

    @authorized
    def getVersion(self, project_id, version_id):

        url = self.api_url + '/data/v1/projects/%s/versions/%s' % (project_id, version_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    @authorized
    def getVersionDownloadFormats(self, project_id, version_id):

        url = self.api_url + '/data/v1/projects/%s/versions/%s/downloadFormats' % (project_id, version_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    @authorized
    def getVersionDownloads(self, project_id, version_id):

        url = self.api_url + '/data/v1/projects/%s/versions/%s/downloads' % (project_id, version_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    @authorized
    def getVersionItem(self, project_id, version_id):

        url = self.api_url + '/data/v1/projects/%s/versions/%s/item' % (project_id, version_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    @authorized
    def getVersionRefs(self, project_id, version_id):

        url = self.api_url + '/data/v1/projects/%s/versions/%s/refs' % (project_id, version_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    @authorized
    def getVersionLinks(self, project_id, version_id):

        url = self.api_url + '/data/v1/projects/%s/versions/%s/links' % (project_id, version_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    @authorized
    def getVersionRelationshipsRefs(self, project_id, version_id):

        url = self.api_url + '/data/v1/projects/%s/versions/%s/relationships/refs' % (project_id, version_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    @authorized
    def patchVersion(self, project_id, version_id, body):

        url = self.api_url + '/data/v1/projects/%s/versions/%s' % (project_id, version_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
            'Content-Type': 'application/vnd.api+json'
        }

        data = body

        return patch_request(url, data, headers)

    @authorized
    def postVersion(self, project_id, body):

        url = self.api_url + '/data/v1/projects/%s/versions' % (project_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
            'Content-Type': 'application/vnd.api+json'
        }

        data = body

        return post_request(url, data, headers)

    @authorized
    def postVersionRelationshipsRefs(self, project_id, version_id, body):

        url = self.api_url + '/data/v1/projects/%s/versions/%s/relationships/refs' % (project_id, version_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
            'Content-Type': 'application/vnd.api+json'
        }

        data = body

        return post_request(url, data, headers)
