from .utils import get_request, post_request, authorized

class Buckets:

    @authorized
    def getBuckets(self):

        url = 'https://developer.api.autodesk.com/oss/v2/buckets'

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)

    @authorized
    def getBucketDetails(self, bucket_key):

        url = 'https://developer.api.autodesk.com/oss/v2/buckets/%s/details' % bucket_key

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token)
        }

        return get_request(url, headers)
        
    @authorized
    def createBucket(self, bucket_key, allow, policy_key):

        url = 'https://developer.api.autodesk.com/oss/v2/buckets'

        headers = {
            'Authorization': '%s %s' % (self.token_type, self.access_token),
            'Content-Type': 'application/json'
        }

        data = {
            'bucketKey': bucket_key,
            'allow': allow,
            'policy_key': policy_key
        }

        return post_request(url, data, headers)
