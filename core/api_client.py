import requests
import json
import allure
from core.sanitizer import sanitize_data

class BaseApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()

    def _send_request(self, method: str, endpoint: str, **kwargs):
        url = f"{self.base_url.rstrip('/')}/{endpoint.strip('/')}"
        if 'timeout' not in kwargs:
            kwargs['timeout'] = 10

        with allure.step(f'API call {method.upper()}, endpoint {endpoint}'):
            if 'json' in kwargs:
                request_json = kwargs['json']
                filtered_json = sanitize_data(request_json)

                allure.attach(
                    body=json.dumps(filtered_json, indent=4, ensure_ascii=False),
                    name='REQUEST JSON',
                    attachment_type=allure.attachment_type.JSON
                )

            if 'data' in kwargs:
                request_data = kwargs['data']
                filtered_data = sanitize_data(request_data)

                allure.attach(
                    body=str(filtered_data),
                    name='REQUEST DATA',
                    attachment_type=allure.attachment_type.TEXT
                )

            response = self.session.request(method=method, url=url, **kwargs)


            # 1. Логируем отправленные заголовки (Request Headers)
            req_headers = dict(response.request.headers)
            safe_req_headers = sanitize_data(req_headers)
            allure.attach(
                body=json.dumps(safe_req_headers, indent=4, ensure_ascii=False),
                name='REQUEST HEADERS',
                attachment_type=allure.attachment_type.JSON
            )

            # 2. Логируем полученные заголовки (Response Headers)
            resp_headers = dict(response.headers)
            safe_resp_headers = sanitize_data(resp_headers)
            allure.attach(
                body=json.dumps(safe_resp_headers, indent=4, ensure_ascii=False),
                name='RESPONSE HEADERS',
                attachment_type=allure.attachment_type.JSON
            )
            
            allure.attach(
                body=response.url,
                name='RESPONSE URL',
                attachment_type=allure.attachment_type.TEXT
            )

            allure.attach(
                body=str(response.status_code),
                name='RESPONSE STATUS CODE',
                attachment_type=allure.attachment_type.TEXT
            )


            try:
                response_json = response.json()
                filtered_resp_json = sanitize_data(response_json)

                allure.attach(
                    body=json.dumps(filtered_resp_json, indent=4, ensure_ascii=False),
                    name='RESPONSE JSON',
                    attachment_type=allure.attachment_type.JSON
                )

            except json.JSONDecodeError:

                allure.attach(
                    body=response.text,
                    name='RESPONSE TEXT',
                    attachment_type=allure.attachment_type.TEXT
                )

        return response


    def get(self, endpoint:str, **kwargs):
        return self._send_request('GET', endpoint, **kwargs)

    def post(self, endpoint:str, **kwargs):
        return self._send_request('POST', endpoint, **kwargs)

    def put(self, endpoint:str, **kwargs):
        return self._send_request('PUT', endpoint, **kwargs)

    def delete(self, endpoint:str, **kwargs):
        return self._send_request('DELETE', endpoint, **kwargs)

if __name__ == '__main__':
    client = BaseApiClient('https://jsonplaceholder.typicode.com')
    response = client.get('/posts/1')
    print(response.status_code)