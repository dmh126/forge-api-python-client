from .utils import get_request, post_request, patch_request, put_request, delete_request
import os

class Objects:

    def putObject(self, fpath, bucket_key, object_name):

        url = 'https://developer.api.autodesk.com/oss/v2/buckets/%s/objects/%s' % (bucket_key, object_name)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
            'Content-Type': 'application/octet-stream',
            'Content-Length': os.path.getsize(fpath)
        }

        return put_request(url, fpath, headers)

    def putObjectResumable(self, fpath, bucket_key, object_name):

        url = 'https://developer.api.autodesk.com/oss/v2/buckets/%s/objects/%s/resumable' % (bucket_key, object_name)

        # TODO

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
            'Content-Type': 'application/octet-stream',
            'Content-Length': os.path.getsize(fpath)
        }

        return put_request(url, fpath, headers)

    def getObjectSession(self, bucket_key, object_name, session_id):

        url = 'https://developer.api.autodesk.com/oss/v2/buckets/%s/objects/%s/status/%s' % (bucket_key, object_name, session_id)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
        }

        return get_request(url, headers)

    def getObjects(self, bucket_key):

        url = 'https://developer.api.autodesk.com/oss/v2/buckets/%s/objects' % (bucket_key)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
        }

        return get_request(url, headers)

    def getObjectDetails(self, bucket_key, object_name):

        url = 'https://developer.api.autodesk.com/oss/v2/buckets/%s/objects/%s/details' % (bucket_key, object_name)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
        }

        return get_request(url, headers)

    def getObject(self, bucket_key, object_name):

        url = 'https://developer.api.autodesk.com/oss/v2/buckets/%s/objects/%s' % (bucket_key, object_name)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
        }

        return get_request(url, headers)

    def postObjectSigned(self, data, bucket_key, object_name):

        url = 'https://developer.api.autodesk.com/oss/v2/buckets/%s/objects/%s/signed' % (bucket_key, object_name)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
            'Content-Type': 'application/json'
        }

        return post_request(url, data, headers)

    def putSignedResource(self, fpath, id):

        url = 'https://developer.api.autodesk.com/oss/v2/signedresources/%s' % id

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
            'Content-Type': 'application/json'
        }

        return put_request(url, fpath, headers)

    def putSignedResourceResumable(self, fpath, id, session_id, content_range):

        url = 'https://developer.api.autodesk.com/oss/v2/signedresources/%s' % id

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
            'Session-Id': session_id,
            'Content-Range': content_range
        }

        return put_request(url, fpath, headers)

    def getSignedResource(self, id):

        url = 'https://developer.api.autodesk.com/oss/v2/signedresources/%s' % id

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
        }

        return get_request(url, headers)

    def deleteSignedResource(self, id):

        url = 'https://developer.api.autodesk.com/oss/v2/signedresources/%s' % id

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
        }

        return delete_request(url, headers)

    def copyObject(self, bucket_key, object_name, new_name):

        url = 'https://developer.api.autodesk.com/oss/v2/buckets/%s/objects/%s/copyto/%s' % (bucket_key, object_name, new_name)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
        }

        fpath = None

        return put_request(url, fpath, headers)

    def deleteObject(self, bucket_key, object_name):

        url = 'https://developer.api.autodesk.com/oss/v2/buckets/%s/objects/%s' % (bucket_key, object_name)

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
        }

        return delete_request(url, headers)
