from urllib.parse import urljoin
import requests


class JSONErrorException(Exception):
    pass


class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def request_advanced(
        self,
        method,
        url=None,
        location=None,
        headers=None,
        data=None,
        params=None,
        expected_status=200,
        jsonify=True,
        check_status_code=True
    ):
        if location:
            url = urljoin(self.base_url, location)
        else:
            url = url
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            data=data,
            params=params
        )

        if check_status_code:
            assert (
                response.status_code == expected_status
            ), f"Expected {expected_status}, but got {response.status_code}"

        if jsonify:
            try:
                json_response: dict = response.json()
            except JSONErrorException:
                raise JSONErrorException(
                    f"Expected json response from api request {url}"
                )
            return json_response
        return response
