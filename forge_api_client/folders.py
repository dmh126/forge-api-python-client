from .utils import get_request, post_request, patch_request, authorized

class Folders:

    @authorized
    def getFolder(self, project_id, folder_id):

        url = self.api_url + '/data/v1/projects/%s/folders/%s' % (project_id, folder_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    @authorized
    def getFolderContents(self, project_id, folder_id):

        url = self.api_url + '/data/v1/projects/%s/folders/%s/contents' % (project_id, folder_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    @authorized
    def getFolderParent(self, project_id, folder_id):

        url = self.api_url + '/data/v1/projects/%s/folders/%s/parent' % (project_id, folder_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    @authorized
    def getFolderRefs(self, project_id, folder_id):

        url = self.api_url + '/data/v1/projects/%s/folders/%s/refs' % (project_id, folder_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    @authorized
    def getFolderRelationshipsLinks(self, project_id, folder_id):

        url = self.api_url + '/data/v1/projects/%s/folders/%s/relationships/links' % (project_id, folder_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    @authorized
    def getFolderRelationshipsRefs(self, project_id, folder_id):

        url = self.api_url + '/data/v1/projects/%s/folders/%s/relationships/refs' % (project_id, folder_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    @authorized
    def getFolderSearch(self, project_id, folder_id):

        #TODO

        url = self.api_url + '/data/v1/projects/%s/folders/%s/search' % (project_id, folder_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    @authorized
    def patchFolder(self, project_id, folder_id, body):

        url = self.api_url + '/data/v1/projects/%s/folders/%s' % (project_id, folder_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
            'Content-Type': 'application/vnd.api+json'
        }

        data = body

        return patch_request(url, data, headers)

    @authorized
    def postFolder(self, project_id, body):

        url = self.api_url + '/data/v1/projects/%s/folders' % (project_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
            'Content-Type': 'application/vnd.api+json'
        }

        data = body

        return post_request(url, data, headers)

    @authorized
    def postFolderRelationshipsRefs(self, project_id, folder_id, body):

        url = self.api_url + '/data/v1/projects/%s/folders/%s/relationships/refs' % (folder_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
            'Content-Type': 'application/vnd.api+json'
        }

        data = body

        return post_request(url, data, headers)
