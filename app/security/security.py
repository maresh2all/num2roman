import hmac
import hashlib
import base64

from functools import lru_cache
from .. import config

@lru_cache()
def get_settings():
    return config.Settings()


settings=get_settings()

def hash_api_key_hmac(api_key: str, api_secret: str):
    dig = hmac.new(bytes(api_secret, 'utf-8'), msg=bytes(api_key, 'utf-8'), digestmod=hashlib.sha256).digest()
    return base64.b64encode(dig).decode()

def validate_api_key(api_key: str, method: str = 'basic_auth') -> bool:
    if method == 'basic_auth':
        return (api_key == settings.API_KEY)
    elif method == 'hmac':
        api_key_hashed  = hash_api_key_hmac(api_key, settings.API_SECRET)
        return (api_key_hashed == settings.API_KEY_HASHED)
    else:
        raise Exception('Unsupported "{}" API KEY validation method.'.format(method))