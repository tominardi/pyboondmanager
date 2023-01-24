import contextlib
import json
import os

from bottle import route, run, template, request

from boondmanager.api import BoondmanagerClient
from boondmanager.auth import decode_boondmanager_payload, get_jwt


BOONDMANAGER_APP_KEY = '123456789'


@route('/')
def index():
    return template('<b>Hello {{name}}</b>!', name='boondmanager')


@route('/current-user')
def current_user():
    # Read the signed request to get the user token
    signed_request = request.forms.get('signedRequest')
    if not signed_request:
        return 'out of context'
    payload = decode_boondmanager_payload(signed_request, BOONDMANAGER_APP_KEY)
    with open('settings.json', 'w', encoding='utf-8') as settings_file:
        settings = json.load(settings_file)
    jwt = get_jwt(
        user_token=settings.get('user_token'),
        client_key=BOONDMANAGER_APP_KEY,
        client_token=payload.get('client_token')
    )
    client = BoondmanagerClient(jwt_app=jwt)
    current_users = client.users.application_current_user.all()
    return f'Hello {current_users[0].attributes.first_name}'  # TODO implement this


@route('/install', method='POST')
def install():
    signed_request = request.forms.get('signedRequest')
    payload = decode_boondmanager_payload(signed_request, BOONDMANAGER_APP_KEY)
    settings = {
        'client_token': payload.get('clientToken'),
        'client_name': payload.get('clientName'),
        'app_token': payload.get('appToken'),
        'refresh_token': payload.get('refreshToken'),
        'created_at': payload.get('createdAt'),
        'expires_in': payload.get('expiresIn'),
        'installation_code': payload.get('installationCode'),
        'issued_at': payload.get('issuedAt'),
        'expiration_date': payload.get('expirationDate'),
    }
    with open('settings.json', 'w', encoding='utf-8') as settings_file:
        json.dump(settings, settings_file)
    response_data = {'result': True}
    json.dumps(response_data)


@route('/uninstall', method='DELETE')
def uninstall():
    # delete the settings.json file on the filesystem
    with contextlib.suppress(OSError):
        os.remove('settings.json')
    response_data = {'result': True}
    # return a string representation of response_data
    return json.dumps(response_data)


run(host='0.0.0.0', port=8080)
