import requests
import json
import exceptions


class Client(object):
    api_key = None
    headers = {}

    def __init__(self, api_key, base='https://api.freecurrencyapi.com/v1'):
        if api_key:
            self.headers['apikey'] = api_key
        self.api_base = base

    @staticmethod
    def _request(method="GET", url='https://api.freecurrencyapi.com/v1', headers=None, params=None):
        if params is None:
            params = dict()
        if headers is None:
            headers = dict()
        response = requests.request(method, url, headers=headers, params=params)
        if response:
            if response.status_code == 200:
                return response
            elif response.status_code == 429:
                if 'x-ratelimit-remaining-quota-month' in response.headers:
                    quota = response.headers['x-ratelimit-remaining-quota-month']
                    if int(quota) <= 0:
                        raise exceptions.QuotaExceeded(response.text)
                    raise exceptions.RateLimitExceeded(response.text)
            elif response.status_code == 403:
                raise exceptions.NotAllowed(response.text)

            elif response.status_code == 401:
                raise exceptions.IncorrectApikey(response.text)

            elif response.status_code == 404:
                raise exceptions.NotFound(response.text)

            elif response.status_code == 422:
                raise exceptions.ValidationError(response.text)

            else:
                raise exceptions.OtherError(response.text)
        else:
            raise exceptions.EmptyResponse(response.text)

    def status(self):
        """
        Get the status of the API
        :return: Status and quotas
        """
        url = self.api_base + '/status'
        response = self._request(url=url, headers=self.headers)
        status = response.status_code
        response_obj = json.loads(response.text)
        return status, response_obj['quotas']

    def get_currencies(self, currencies=None):
        """
        Get the list of currencies
        :param currencies: List of currencies
        :return: Dict of currencies
        """
        if currencies is None:
            currencies = []
        url = self.api_base + '/currencies'
        params = {'currencies': ','.join(currencies)}
        response = self._request(url=url, headers=self.headers, params=params)
        response_obj = json.loads(response.text)
        response_data = dict(response_obj['data'])
        for key, value in response_data.items():
            print("|", f"{key:>4}", "|", f"{value['symbol'] :>4}", "|", f"{value['name'] :<25}|")

    def latest(self, base_currency=None, currencies=None, amount=1):
        """
        Get the latest exchange rates
        :param base_currency: Base currency
        :param currencies: List of currencies
        :param amount: Amount of base currency
        :return:
        """
        if currencies is None:
            currencies = list()
        url = self.api_base + '/latest'
        params = {'base': base_currency, 'currencies': ','.join(currencies)}
        response = self._request(url=url, headers=self.headers, params=params)
        response_obj = json.loads(response.text)
        return {i: j * amount for i, j in response_obj['data'].items()}

    def historical(self, date, base_currency=None, currencies=None, amount=1):
        """
        Get historical exchange rates
        :param date: YYYY-MM-DD
        :param base_currency: Base currency
        :param currencies: List of currencies
        :param amount: Amount of base currency
        :return: Dict of currencies
        """
        if currencies is None:
            currencies = list()
        url = self.api_base + '/historical'
        params = {'date': date, 'base': base_currency, 'currencies': ','.join(currencies)}
        response = self._request(url=url, headers=self.headers, params=params)
        response_obj = json.loads(response.text)
        return {i: j * amount for i, j in response_obj['data'][date].items()}
