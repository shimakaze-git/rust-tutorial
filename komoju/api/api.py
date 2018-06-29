# -*- coding: utf-8 -*-
'''
Created on 2018/06/27

@author: shimakaze-git
'''
from conf import API_ENDPOINT

from requests.auth import HTTPBasicAuth
import requests

class KomojuApi():
    """Komoju API Base class"""

    def __init__(self, api_key):
        self.api_endpoint = API_ENDPOINT
        self.basic_auth = HTTPBasicAuth(api_key, '')

    def get_request(self, api_endpoint):
        """GET Request
        :param api_endpoint: api_endpoint_url 
        :type api_endpoint: str 
        :returns: response
        :rtype: dict
        """
        try:
            res = requests.get(api_endpoint, auth=self.basic_auth)
            if res.status_code == requests.codes.ok:
                return res.json()
            else:
                return res.json()
        except Exception as ex:
            res = {
                'error': None
            }
            return res
    
    def post_request(self, api_endpoint, data):
        """POST Request
        :param api_endpoint: api_endpoint_url
        :type api_endpoint: str
        :param data: post_data
        :type data: dict
        
        :returns: response
        :rtype: dict
        """
        try:
            res = requests.post(api_endpoint, data=data)
            if res.status_code == requests.codes.ok:
                return res.json()
            else:
                return res.json()
        except Exception as ex:
            res = {
                'error': None
            }
            return res