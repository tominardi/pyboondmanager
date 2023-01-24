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
        self._reset()
        self.response = self._send(session, prepped)
        if self.response.status_code == 404:
            raise PageNotFoundError()
        if self.response.status_code == 422:
            messages = []
            for error in self.response.json().get('errors'):
                if error.get('detail') not in messages:
                    messages.append(error.get('detail'))
            raise BoondManagerUnprocessableEntity(', '.join(messages))
        self._build_response_data()
        return self.data


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
    resource_id = None
    auth = None
    headers = {}
    post_data = {}
    meta = {}
    data = None
    included = []
    response = None
    client = None
    query_params = None
    _domain = None

    def __init__(self, basic_auth=None, jwt_app=None, jwt_client=None, resource_id=None, domain=None):
        self.client = requests
        self.resource_id = resource_id
        if basic_auth:
            self.auth = self.client.auth.HTTPBasicAuth(basic_auth.get('user'),
                                                       basic_auth.get('password'))
        self.jwt_app = jwt_app
        self.jwt_client = jwt_client
        self._domain = domain or BOONDMANAGER_API_URL

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

    def _reset(self):
        """
        reset the given object before launching a request
        """
        self.meta = {}
        self.data = None
        self.included = []
        self.response = None

    def _build_response_data(self):
        response_json = self.response.json()
        self.meta = response_json.get('meta')
        # response data could be a list or a dict
        if isinstance(response_json.get('data'), list):
            self.data = [JsonAPIData(response_data) for response_data in response_json.get('data', [])]
        else:
            self.data = JsonAPIData(response_json.get('data', {}))
        for include in response_json.get('included', []):
            self.included.append(JsonAPIData(include))

    def set_headers(self, headers):
        """
        Replace the current headers with the given headers
        """
        if not isinstance(headers, dict):
            raise TypeError(f'headers should be a dict, not {type(headers).__name__}')
        self.headers = headers

    def add_header(self, name, value):
        """
        Add a header to the current headers

        :param name: The name of the header
        :param value: The value of the header
        """
        self.headers[name] = value

    def reset_headers(self):
        """
        Reset the headers
        """
        self.headers = {}

    def set_query_params(self, query_params):
        """
        Replace the current query params with the given query_params
        """
        if not isinstance(query_params, dict):
            raise TypeError(f'query params should be a dict, not {type(query_params).__name__}')
        self.query_params = query_params

    def add_query_param(self, name, value):
        """
        Add a query param to the current query params

        :param name: The name of the query param
        :param value: The value of the query param
        """
        self.query_params[name] = value

    def reset_query_params(self):
        """
        Reset the query params
        """
        self.query_params = None

    def _send(self, session, prepped):  # pragma: no cover
        return session.send(prepped, timeout=DEFAULT_TIMEOUT)

    def _set_headers(self):
        if not self.headers:
            self.headers = {}
        if self.jwt_app:
            self.headers['X-Jwt-App-Boondmanager'] = self.jwt_app
        if self.jwt_client:
            self.headers['X-Jwt-Client-Boondmanager'] = self.jwt_client

    def request(self, method, resource_id=None, post_data=None, tab_name=None, forced_uri=None):
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
        if resource_id:
            self.resource_id = resource_id
        if post_data:
            self.post_data = post_data
        session = self.client.Session()
        url = self._make_url(self.resource_id, tab_name, forced_uri=forced_uri)
        req = self.client.Request(method, url)
        if self.auth:
            req.auth = self.auth
        if self.query_params:
            req.params = self.query_params
        if self.headers or self.jwt_client or self.jwt_app:
            self._set_headers()
            req.headers = self.headers
        if self.post_data:
            req.data = self.post_data
        prepped = req.prepare()
        self._reset()
        self.response = self._send(session, prepped)
        if self.response.status_code == 403:
            raise BoondManagerForbidden()
        if self.response.status_code == 404:
            raise PageNotFoundError()
        if self.response.status_code == 422:
            messages = []
            for error in self.response.json().get('errors'):
                if error.get('detail') not in messages:
                    messages.append(error.get('detail'))
            raise BoondManagerUnprocessableEntity(', '.join(messages))
        self._build_response_data()
        return self.data

    def get(self, resource_id=None, params=None):
        """
        Make a get request to the API

        :param resource_id: The id of the content to work on (default: None)
        """
        if params:
            self.set_query_params(params)
        return self.request('GET', resource_id=resource_id)

    def get_tab(self, resource_id, tab_name):
        """
        Make a get request to the API on a specific tab

        :param resource_id: The id of the content to work on
        :param tab_name: The tab to use
        """
        return self.request('GET', resource_id=resource_id, tab_name=tab_name)

    def all(self, params=None):
        """Alias for get with no resource_id"""
        self.resource_id = None
        return self.get(params=params)

    def post(self, data=None):
        """
        Make a post request to the API

        :param data: The data to send in the request (default: None)
        """
        self.add_header('content-type', 'application/json')
        return self.request('POST', post_data=data)

    def post_tab(self, resource_id, tab_name, data=None):
        """
        Make a get request to the API on a specific tab

        :param resource_id: The id of the content to work on
        :param tab_name: The tab to use
        """
        self.add_header('content-type', 'application/json')
        return self.request('GET', resource_id=resource_id, tab_name=tab_name, post_data=data)

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
