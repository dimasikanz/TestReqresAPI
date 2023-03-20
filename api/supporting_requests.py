from .apiclient import ApiClient
from lib.apis import APILocations

def create_new_user(api_client: ApiClient, email:str , password: str):
    data = {'email': email,
            'password': password}
    response = api_client.request_advanced(method='POST', location=APILocations.REGISTER_LOCATION, data=data)
    return {'id': response['id'], 'token': response['token']}