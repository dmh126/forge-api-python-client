import requests
import os

def get_request(url, headers={}):

    req = requests.get(url, headers=headers)

    return req.json()

def post_request(url, data, headers={}):

    req = requests.post(url, data=data, headers=headers)

    return req.json()

def patch_request(url, data, headers={}):

    req = requests.patch(url, data=data, headers=headers)

    return req.json()

def put_request(url, fpath, headers={}):

    if fpath:

        f = open(fpath, 'rb').read()

        req = requests.put(url, data=f, headers=headers)

    else:

        req = requests.put(url, headers=headers)

    return req.json()

def delete_request(url, headers={}):

    req = requests.delete(url, headers=headers)

    return req.json()
