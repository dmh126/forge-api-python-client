import requests
import os

def get_request(url, headers={}):

    try:

        res = requests.get(url, headers=headers)

    except requests.exceptions.RequestException as e:

        raise e

    if not res.status_code // 100 == 2:

        res.raise_for_status()

    else:

        return res.json()

def post_request(url, data, headers={}):

    try:

        res = requests.post(url, data=data, headers=headers)

    except requests.exceptions.RequestException as e:

        raise e

    if not res.status_code // 100 == 2:

        res.raise_for_status()

    else:

        return res.json()


def patch_request(url, data, headers={}):

    try:

        res = requests.patch(url, data=data, headers=headers)

    except requests.exceptions.RequestException as e:

        raise e

    if not res.status_code // 100 == 2:

        res.raise_for_status()

    else:

        return res.json()

def put_request(url, fpath, headers={}):

    try:

        if fpath:

            f = open(fpath, 'rb').read()

            res = requests.put(url, data=f, headers=headers)

        else:

            res = requests.put(url, headers=headers)

    except requests.exceptions.RequestException as e:

        raise e

    if not res.status_code // 100 == 2:

        res.raise_for_status()

    else:

        return res.json()

def delete_request(url, headers={}):

    try:

        res = requests.delete(url, headers=headers)

    except requests.exceptions.RequestException as e:

        raise e

    if not res.status_code // 100 == 2:

        res.raise_for_status()

    else:

        return res.json()


def authorized(func):
    """
    A decorator. Use to check if user has been authorized without calling the API and retrieving errors.
    """
    def _authorized(self, *args, **kwargs):

        if not self.access_token:

            raise RuntimeError(
            """
            No Access Token found. User must be authorized. Please invoke an authentication method first.

            Example:

            from forge_api_client import ApiClient

            >>> client_id = 'your_client_id'
            >>> client_secret = 'client_secret'
            >>> scope = 'bucket:read' # ex. 'data:read'
            >>> fac = ApiClient()
            >>> fac.authClientTwoLegged(client_id, client_secret, scope=scope)
            >>> buckets = fac.getBuckets()
            """)
        else:

            return func(self, *args, **kwargs)

    return _authorized
