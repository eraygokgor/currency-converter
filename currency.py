import requests
import json


class Client(object):
    api_key = None
    headers = {}

    def __init__(self, api_key, base='https://api.freecurrencyapi.com/v1'):
        if api_key:
            self.headers['apikey'] = api_key
        self.api_base = base

    def status(self):
        method = 'GET'
        url = self.api_base + '/status'
        response = requests.request(method, url, headers=self.headers)
        status = response.status_code
        response_obj = json.loads(response.text)
        return status, response_obj['quotas']

    def get_currencies(self, currencies=None, more_info=False):
        if currencies is None:
            currencies = []
        method = 'GET'
        url = self.api_base + '/currencies'
        params = {'currencies': ','.join(currencies)}
        response = requests.request(method, url, headers=self.headers, params=params)
        response_obj = json.loads(response.text)
        response_data = dict(response_obj['data'])
        for key, value in response_data.items():
            if more_info:
                print("|", f"{key:>4}", "|", f"{value['symbol'] :>4}", "|", f"{value['name'] :<25}|")
            else:
                print(key)

    def latest(self, base_currency=None, currencies=None):
        if currencies is None:
            currencies = []
        method = 'GET'
        url = self.api_base + '/latest'
        params = {'base': base_currency, 'currencies': ','.join(currencies)}
        response = requests.request(method, url, headers=self.headers, params=params)
        response_obj = json.loads(response.text)
        return response_obj['data']

    def historical(self, date, base_currency=None, currencies=None):
        if currencies is None:
            currencies = []
        method = 'GET'
        url = self.api_base + '/historical'
        params = {'date': date, 'base': base_currency, 'currencies': ','.join(currencies)}
        response = requests.request(method, url, headers=self.headers, params=params)
        response_obj = json.loads(response.text)
        return response_obj['data']
