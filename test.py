import os
import unittest
from forge_api_client import ApiClient

class Tests(unittest.TestCase):

    def setUp(self):
        self.client_id = os.environ["FORGE_CLIENT_ID"]
        self.client_secret = os.environ["FORGE_CLIENT_SECRET"]

    def test_buckets(self):
        fac = ApiClient()
        fac.authClientTwoLegged(self.client_id, self.client_secret, scope="bucket:read")
        buckets = fac.getBuckets()
        self.assertIn("items", buckets)

if __name__ == '__main__':
    unittest.main()
