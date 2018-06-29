# -*- coding: utf-8 -*-
'''
Created on 2018/06/27

@author: shimakaze-git
'''
import urllib.request
from api import KomojuApi

from requests.auth import HTTPBasicAuth
import requests, json

class PaymentsApi(KomojuApi):
    """PaymentsApi class"""

    def __init__(self, api_key):
        self.api_key = api_key
        
        super(PaymentsApi, self).__init__(api_key)
        self.api_endpoint = self.api_endpoint + "payments"

    def get_payments(self):
        response = self.get_request(self.api_endpoint)
        return response

    def get_payment_id(self, payment_id):
        api_endpoint_url = self.api_endpoint + '/' + str(payment_id)
        response = self.get_request(api_endpoint_url)
        return response

    def post_payment(self, amount, currency, external_order_num, payment_details, metadata=None):
        payload = {
            'amount': str(amount),
            'currency': str(currency),
            'external_order_num': str(external_order_num)
        }

        """payment_details."""
        for param in payment_details:
            payload['payment_details['+str(param)+']'] = str(payment_details[param])

        """metadata."""
        if metadata is not None:
            for meta in metadata:
                payload['metadata['+str(meta)+']'] = metadata[meta]

        post_data = json.dumps(payload)
        response = self.post_request(
            self.api_endpoint,
            post_data
        )
        return response

if __name__ == '__main__':
    api_key = ""
    test = PaymentsApi(api_key)
