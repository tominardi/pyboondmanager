# Copyright (c) 2023 Thomas Durey

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests

from boondmanager.exceptions import (BoondManagerUnprocessableEntity, MethodNotAllowed, NoSingleUrl, PageNotFoundError,
                                     UnknownTab, BoondManagerForbidden)
from boondmanager.utils import JsonAPIData


BOONDMANAGER_API_URL = 'https://ui.boondmanager.com/api'  # Default API URL
DEFAULT_TIMEOUT = 30  # Default timeout for requests


class DefaultEndpointMixin():
    """
    Mixin for default endpoint implementation
    """

    def get_default(self, params=None):
        url = f'{self._domain}{self.list_uri}/default'
        session = self.client.Session()
        req = self.client.Request('GET', url, auth=self.auth)
        if params:
            req.params = params
        prepped = req.prepare()
        response = self._send(session, prepped)
        if response.status_code == 404:
            raise PageNotFoundError()
        if response.status_code == 422:
            messages = []
            for error in response.json().get('errors'):
                if error.get('detail') not in messages:
                    messages.append(error.get('detail'))
            raise BoondManagerUnprocessableEntity(', '.join(messages))
        data = self._build_response_data(response)
        return data


class BaseClient:
    """
    Base API interface

    :param basic_auth: Dictionnary containing user and password keys
    :param jwt_app: The JWT token for the app
    :param jwt_client: The JWT token for the client
    :param resource_id: The id of the content to work on
    :param domain: The domain to request on. If null, use BOONDMANAGER_API_URL

    - TODO: We want different allowed methods given the used uri
    """

    # pylint: disable=too-many-instance-attributes

    allowed_methods = []
    list_uri = None
    single_uri = None
    tabs = []
    auth = None
    client = None
    _domain = None
    session = None

    def __init__(self, *, basic_auth=None, jwt_app=None, jwt_client=None, domain=None):
        self.client = requests
        if basic_auth:
            self.auth = self.client.auth.HTTPBasicAuth(basic_auth.get('user'),
                                                       basic_auth.get('password'))
        self.jwt_app = jwt_app
        self.jwt_client = jwt_client
        self._domain = domain or BOONDMANAGER_API_URL
        self.session = self.client.Session()

    def _make_url(self, resource_id=None, tab_name=None, forced_uri=None):
        """
        Construct URL from list
        """
        if resource_id and not self.single_uri:
            raise NoSingleUrl()
        if tab_name and tab_name not in self.tabs:
            raise UnknownTab()
        if forced_uri:
            return f'{self._domain}{forced_uri}'
        if resource_id:
            uri = self.single_uri.format(resource_id)
            if tab_name:
                uri = f'{uri}/{tab_name}'
            return f'{self._domain}{uri}'
        return f'{self._domain}{self.list_uri}'

    def _build_response_data(self, response):
        response_json = response.json()
        # response data could be a list or a dict
        if isinstance(response_json.get('data'), list):
            data = [JsonAPIData(response_data) for response_data in response_json.get('data', [])]
        else:
            data = JsonAPIData(response_json.get('data', {}))
        return data

    def _send(self, session, prepped):  # pragma: no cover
        return session.send(prepped, timeout=DEFAULT_TIMEOUT)

    def _set_headers(self, headers):
        if not headers:
            headers = {}
        if self.jwt_app:
            headers['X-Jwt-App-Boondmanager'] = self.jwt_app
        if self.jwt_client:
            headers['X-Jwt-Client-Boondmanager'] = self.jwt_client
        return headers

    def request(self, method, *, resource_id=None, post_data=None, tab_name=None, forced_uri=None, query_params=None):
        """
        Make a request to the API

        :param method: The method to use
        :param resource_id: The id of the content to work on (default: None)
        :param post_data: The data to send in the request (default: None)
        :param tab_name: The tab to use (default: None)
        :param forced_uri: Force an uri manually (default: None)
        """
        if method not in self.allowed_methods:
            raise MethodNotAllowed()
        headers = {}
        if post_data:
            headers['content-type'] = 'application/json'
        # session = self.client.Session()
        url = self._make_url(resource_id, tab_name, forced_uri=forced_uri)
        req = self.client.Request(method, url)
        if self.auth:
            req.auth = self.auth
        if query_params:
            req.params = query_params
        if headers or self.jwt_client or self.jwt_app:
            headers = self._set_headers(headers)
            req.headers = headers
        if post_data:
            req.data = post_data
        prepped = req.prepare()
        response = self._send(self.session, prepped)
        if response.status_code == 403:
            raise BoondManagerForbidden()
        if response.status_code == 404:
            raise PageNotFoundError()
        if response.status_code == 422:
            messages = []
            for error in response.json().get('errors'):
                if error.get('detail') not in messages:
                    messages.append(error.get('detail'))
            raise BoondManagerUnprocessableEntity(', '.join(messages))
        data = self._build_response_data(response)
        return data

    def get(self, resource_id=None, params=None):
        """
        Make a get request to the API

        :param resource_id: The id of the content to work on (default: None)
        """
        if params:
            if not isinstance(params, dict):
                raise TypeError(f'params for a get should be a dict, not {type(params).__name__}')
        return self.request('GET', resource_id=resource_id, query_params=params)

    def get_tab(self, resource_id, tab_name):
        """
        Make a get request to the API on a specific tab

        :param resource_id: The id of the content to work on
        :param tab_name: The tab to use
        """
        return self.request('GET', resource_id=resource_id, tab_name=tab_name)

    def all(self, params=None):
        """Alias for get with no resource_id"""
        return self.get(params=params)

    def post(self, data=None):
        """
        Make a post request to the API

        :param data: The data to send in the request (default: None)
        """
        return self.request('POST', post_data=data)

    def post_tab(self, resource_id, tab_name, data=None):
        """
        Make a get request to the API on a specific tab

        :param resource_id: The id of the content to work on
        :param tab_name: The tab to use
        """
        return self.request('POST', resource_id=resource_id, tab_name=tab_name, post_data=data)

    def put(self, resource_id=None, data=None, tab_name=None):
        """
        Make a put request to the API

        :param resource_id: The id of the content to work on (default: None)
        :param data: The data to send in the request (default: None)
        :param tab_name: The tab to use (default: None)
        """
        return self.request('PUT', resource_id=resource_id, post_data=data, tab_name=tab_name)

    def patch(self, resource_id=None, data=None, tab_name=None):
        """
        Make a patch request to the API

        :param resource_id: The id of the content to work on (default: None)
        :param data: The data to send in the request (default: None)
        :param tab_name: The tab to use (default: None)
        """
        return self.request('PATCH', resource_id=resource_id, post_data=data, tab_name=tab_name)

    def delete(self, resource_id=None):
        """
        Make a delete request to the API

        :param resource_id: The id of the content to work on (default: None)
        """
        return self.request('DELETE', resource_id=resource_id)

    def options(self, resource_id=None, tab_name=None):
        """
        Make a options request to the API

        :param resource_id: The id of the content to work on (default: None)
        :param tab_name: The tab to use (default: None)
        """
        return self.request('OPTIONS', resource_id=resource_id, tab_name=tab_name)
