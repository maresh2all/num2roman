from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
import requests
import os
load_dotenv()

URL_API = 'http://127.0.0.1:8000/api/v0' # FastAPI
headers={'api_key': os.environ['API_KEY']}  

def call_roman_api(n: int):
    '''send request'''

    url_request = '{0}/num2roman/{1}'.format(URL_API, n)
    response = requests.post(url_request,
                            headers = headers,
                            verify=False, stream=False)

    if response.status_code == 200:
        print('Response: {}'.format(response.json(), indent=2))
    else:
        print(response.content)
        raise Exception(response)

call_roman_api(10)
call_roman_api(12)
call_roman_api("2test")