from .utils import get_request, post_request, authorized

class Projects:

    @authorized
    def getProjects(self, hub_id):

        url = 'https://developer.api.autodesk.com/project/v1/hubs/%s/projects' % hub_id

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    @authorized
    def getProject(self, hub_id, project_id):

        url = 'https://developer.api.autodesk.com/project/v1/hubs/%s/projects/%s' % (hub_id, project_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    @authorized
    def getProjectHub(self, hub_id, project_id):

        url = 'https://developer.api.autodesk.com/project/v1/hubs/%s/projects/%s/hub' % (hub_id, project_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    @authorized
    def getTopFolders(self, hub_id, project_id):

        url = 'https://developer.api.autodesk.com/project/v1/hubs/%s/projects/%s/topFolders' % (hub_id, project_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    @authorized
    def getDownload(self, project_id, download_id):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/downloads/%s' % (project_id, download_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    @authorized
    def getJobs(self, project_id, job_id):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/jobs/%s' % (project_id, job_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    @authorized
    def postDownload(self, project_id, body):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/downloads' % (project_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
            'Content-Type': 'application/vnd.api+json'
        }

        data = body

        return post_request(url, data, headers)

    @authorized
    def postStorage(self, project_id, body):

        url = 'https://developer.api.autodesk.com/data/v1/projects/%s/storage' % (project_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
            'Content-Type': 'application/vnd.api+json'
        }

        data = body

        return post_request(url, data, headers)
