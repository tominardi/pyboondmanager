"""
Copyright (c) 2023 Thomas Durey

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import base64
import hmac
import hashlib
import json

import time


HEADER = {
    'alg': 'HS256',
    'typ': 'JWT'
}


def decode_boondmanager_payload(signed_request, boondmanager_app_key):
    """
    Decode a BoondManager signed request

    Warning: we use here the hexdigest() method of the hmac module, which is not
    always used everywere. See the get_signature() method for more details.

    :param signed_request: The signed request
    :param boondmanager_app_key: The BoondManager app key
    :return: The decoded payload
    """
    encoded_signature, payload = signed_request.split('.')
    signature = hmac.new(
        bytes(boondmanager_app_key, encoding='utf-8'),
        bytes(payload, encoding='utf-8'),
        hashlib.sha256).hexdigest()
    if base64_url_decode(encoded_signature) == signature:
        return json.loads(base64_url_decode(payload))
    return False  # pragma: no cover


def base64_url_encode(str_to_encode):
    return base64.urlsafe_b64encode(
        bytes(str_to_encode, encoding='utf-8')).rstrip(b'=').replace(b'/', b'_').replace(b'+', b'-').decode('utf-8')


def base64_url_decode(str_to_decode):
    return base64.urlsafe_b64decode(
        bytes(str_to_decode, encoding='utf-8') + b'=' * (4 - len(str_to_decode) % 4)).decode('utf-8')


def get_signature(encoded_header, encoded_payload, client_key):
    hmac_signature = hmac.new(
        bytes(client_key, encoding='utf-8'),
        bytes(f'{encoded_header}.{encoded_payload}', encoding='utf-8'),
        hashlib.sha256,
    ).digest()
    return base64.urlsafe_b64encode(hmac_signature).rstrip(b'=').replace(b'/', b'_').replace(b'+', b'-').decode('utf-8')


def get_jwt(user_token, client_token, client_key, mode='normal', timestamp=None):
    """
    :param user_token: user token
    :param client_token: client token or app token
    :param client_key: client key or app key
    :param mode: normal or god
    :param timestamp: timestamp in seconds (default: None)
    """
    header = base64_url_encode(json.dumps(HEADER).replace(' ', ''))
    if not timestamp:
        timestamp = time.time()
    payload = {
        'userToken': user_token,
        'clientToken': client_token,
        'time': int(timestamp),
        'mode': mode
    }
    payload = base64_url_encode(json.dumps(payload).replace(' ', ''))
    signature = get_signature(header, payload, client_key)
    return f'{header}.{payload}.{signature}'
