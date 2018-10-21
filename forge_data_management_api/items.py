from .utils import get_request, post_request, patch_request

class Items:

    def getItem(self, project_id, item_id):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/items/%s' % (project_id, item_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    def getItemParent(self, project_id, item_id):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/items/%s/parent' % (project_id, item_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    def getItemRefs(self, project_id, item_id):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/items/%s/refs' % (project_id, item_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    def getItemRelationshipsLinks(self, project_id, item_id):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/items/%s/relationships/links' % (project_id, item_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    def getItemRelationshipsRefs(self, project_id, item_id):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/items/%s/relationships/refs' % (project_id, item_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    def getItemTip(self, project_id, item_id):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/items/%s/tip' % (project_id, item_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    def getItemVersions(self, project_id, item_id):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/items/%s/versions' % (project_id, item_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    def patchItem(self, project_id, item_id, body):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/items/%s' % (project_id, item_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
            'Content-Type': 'application/vnd.api+json'
        }

        data = body

        return patch_request(url, data, headers)


    def postItem(self, project_id, body):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/items' % (project_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
            'Content-Type': 'application/vnd.api+json'
        }

        data = body

        return post_request(url, data, headers)

    def postItemRelationshipsRefs(self, project_id, item_id, body):

        url = '	https://developer.api.autodesk.com/data/v1/projects/%s/items/%s/relationships/refs' % (project_id, item_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
            'Content-Type': 'application/vnd.api+json'
        }

        data = body

        return post_request(url, data, headers)
