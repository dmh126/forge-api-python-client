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
