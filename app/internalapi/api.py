#-*- coding: utf-8 -*-

import requests
import json

class GlobalApi():
    def __init__(self):
        pass
    
    def post(self, endpoint, dictionary):
        url = "http://192.237.219.96:8182/api/v1.0/{0}".format(endpoint)
        header = {'Content-type': 'application/json'}
        req = requests.post(url, data=json.dumps(dictionary), headers=header).json()
        return req

    def put(self, endpoint, case, dictionary):
        url = "http://192.237.219.96:8182/api/v1.0/{0}/{1}".format(endpoint,case)
        header = {'Content-type': 'application/json'}
        req = requests.put(url, data=json.dumps(dictionary), headers=header).json()
        return req

    def get(self, endpoint, case):
        url = "http://192.237.219.96:8182/api/v1.0/{0}/{1}".format(endpoint, case)
        header = {'Content-type': 'application/json'}
        raw = requests.get(url, headers=header).json()
        return raw

    def get_all(self, endpoint):
        url = "http://192.237.219.96:8182/api/v1.0/{0}".format(endpoint)
        header = {'Content-type': 'application/json'}
        raw = requests.get(url, headers=header).json()
        #for t in raw:
        #    if t in endpoint:
        #        print raw[t][0]
        #        foo = json.dumps(raw[t][0])
        #        return foo
        return raw
