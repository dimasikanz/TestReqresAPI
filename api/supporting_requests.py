from .apiclient import ApiClient
from lib.apis import APILocations
from lib.constants import CommonConstants

def create_new_user(api_client: ApiClient,
                    email=CommonConstants.DEFAULT_USER_EMAIL,
                    password=CommonConstants.DEFAULT_USER_PASSWORD):
    data = {'email': email,
            'password': password}
    response = api_client.request_advanced(method='POST', location=APILocations.REGISTER_LOCATION, data=data)
    return {'id': response['id'], 'token': response['token']}