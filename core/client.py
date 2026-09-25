import requests
from requests import Session
from core.sanitizer import sanitize_data

class BaseApiClient():
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()

    def _send_request(self, method: str, endpoint: str, **kwargs):
        full_url = f'{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}'

        raw_headers = kwargs.get('headers')
        raw_json = kwargs.get('json')

        headers = sanitize_data(raw_headers)
        json = sanitize_data(raw_json)

        print(f'[REQUEST]: {method} -> {full_url}')
        print(f'Headers: {headers}')
        print(f'Json: {json}')

        response = self.session.request(method=method, url=full_url, timeout=10, **kwargs)
        print(f'[RESPONSE]: {response.status_code}')

        return response


    def get(self, endpoint: str, **kwargs):
        return self._send_request('GET', endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs):
        return self._send_request('POST', endpoint, **kwargs)

    def patch(self, endpoint: str, **kwargs):
        return self._send_request('PATCH', endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs):
        return self._send_request('DELETE', endpoint, **kwargs)