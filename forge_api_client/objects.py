from .utils import get_request, post_request, patch_request, put_request, delete_request, authorized
import os

class Objects:

    @authorized
    def putObject(self, fpath, bucket_key, object_name):

        url = self.api_url + '/oss/v2/buckets/%s/objects/%s' % (bucket_key, object_name)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
            'Content-Type': 'application/octet-stream',
            'Content-Length': os.path.getsize(fpath)
        }

        return put_request(url, fpath, headers)

    @authorized
    def putObjectResumable(self, fpath, bucket_key, object_name):

        url = self.api_url + '/oss/v2/buckets/%s/objects/%s/resumable' % (bucket_key, object_name)

        # TODO

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
            'Content-Type': 'application/octet-stream',
            'Content-Length': os.path.getsize(fpath)
        }

        return put_request(url, fpath, headers)

    @authorized
    def getObjectSession(self, bucket_key, object_name, session_id):

        url = self.api_url + '/oss/v2/buckets/%s/objects/%s/status/%s' % (bucket_key, object_name, session_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
        }

        return get_request(url, headers)

    @authorized
    def getObjects(self, bucket_key):

        url = self.api_url + '/oss/v2/buckets/%s/objects' % (bucket_key)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
        }

        return get_request(url, headers)

    @authorized
    def getObjectDetails(self, bucket_key, object_name):

        url = self.api_url + '/oss/v2/buckets/%s/objects/%s/details' % (bucket_key, object_name)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
        }

        return get_request(url, headers)

    @authorized
    def getObject(self, bucket_key, object_name):

        url = self.api_url + '/oss/v2/buckets/%s/objects/%s' % (bucket_key, object_name)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
        }

        return get_request(url, headers)

    @authorized
    def postObjectSigned(self, data, bucket_key, object_name):

        url = self.api_url + '/oss/v2/buckets/%s/objects/%s/signed' % (bucket_key, object_name)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
            'Content-Type': 'application/json'
        }

        return post_request(url, data, headers)

    @authorized
    def putSignedResource(self, fpath, id):

        url = self.api_url + '/oss/v2/signedresources/%s' % id

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
            'Content-Type': 'application/json'
        }

        return put_request(url, fpath, headers)

    @authorized
    def putSignedResourceResumable(self, fpath, id, session_id, content_range):

        url = self.api_url + '/oss/v2/signedresources/%s' % id

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
            'Session-Id': session_id,
            'Content-Range': content_range
        }

        return put_request(url, fpath, headers)

    @authorized
    def getSignedResource(self, id):

        url = self.api_url + '/oss/v2/signedresources/%s' % id

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
        }

        return get_request(url, headers)

    @authorized
    def deleteSignedResource(self, id):

        url = self.api_url + '/oss/v2/signedresources/%s' % id

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
        }

        return delete_request(url, headers)

    @authorized
    def copyObject(self, bucket_key, object_name, new_name):

        url = self.api_url + '/oss/v2/buckets/%s/objects/%s/copyto/%s' % (bucket_key, object_name, new_name)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
        }

        fpath = None

        return put_request(url, fpath, headers)

    @authorized
    def deleteObject(self, bucket_key, object_name):

        url = self.api_url + '/oss/v2/buckets/%s/objects/%s' % (bucket_key, object_name)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
        }

        return delete_request(url, headers)
