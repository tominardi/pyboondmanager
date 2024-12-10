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
# pylint: disable=redefined-outer-name

import json
from unittest.mock import MagicMock

import pytest

from boondmanager.auth import get_jwt
from boondmanager.api import BoondmanagerClient
from boondmanager.api.base import BaseClient
from boondmanager.exceptions import (NoSingleUrl, PageNotFoundError, BoondManagerUnprocessableEntity, UnknownTab,
                                     MethodNotAllowed, BoondManagerForbidden)


"""
Ensure that the connectors works as expected.

Note : We don't really send API requests to the server, we just test the
       connector's methods, with a mocked response.
"""


@pytest.fixture()
def client():
    yield BoondmanagerClient(basic_auth={'user': 'test@user', 'password': 'testpassword'})


def save_mock_response(response, filename):
    with open(filename, 'w', encoding='utf-8') as filer:
        json.dump(response.json(), filer, indent=4)


class TestBaseClient:
    """Test the base client."""

    def test_client_request_headers(self, client, mocker):
        client = BaseClient()
        client.allowed_methods = ['GET']
        client.jwt_client = 'mocked_jwt_token'
        mocker.patch.object(client, '_make_url', return_value='http://test.com/resource')
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {}
        mocker.patch.object(client, '_send', return_value=mock_response)
        mock_request = mocker.Mock()
        mocker.patch.object(client.client, 'Request', return_value=mock_request)
        client.get()

        assert mock_request.headers['X-Jwt-Client-Boondmanager'] == 'mocked_jwt_token'

    def test_client_request_params(self, client, mocker):
        client = BaseClient()
        client.allowed_methods = ['GET']
        mocker.patch.object(client, '_make_url', return_value='http://test.com/resource')
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {}
        mocker.patch.object(client, '_send', return_value=mock_response)
        mock_request = mocker.Mock()
        mocker.patch.object(client.client, 'Request', return_value=mock_request)
        query_params = {'key': 'value'}
        client.get(params=query_params)
        assert mock_request.params == {'key': 'value'}

    def test_client_post_headers_data(self, client, mocker):
        client = BaseClient()
        client.allowed_methods = ['POST']
        mocker.patch.object(client, '_make_url', return_value='http://test.com/resource')
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {}
        mocker.patch.object(client, '_send', return_value=mock_response)
        mock_request = mocker.Mock()
        mocker.patch.object(client.client, 'Request', return_value=mock_request)
        client.post({'key': 'value'})
        assert mock_request.data['key'] == 'value'
        assert mock_request.headers['content-type'] == 'application/json'

    def test_method_not_allowed(self):
        """Test that the client raises an exception when the method is not allowed."""
        client = BaseClient()
        with pytest.raises(MethodNotAllowed):
            client.request('GET')

    def test_client_jwt(self, client, mocker):
        client = BaseClient()
        client.allowed_methods = ['GET']
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        jwt = get_jwt(user_token='DIjdfihdè87hdskjhd7879b', client_token='djfdfD90ndlnNoos', client_key='dskjfhdsf')
        client.jwt_client = jwt
        with open('tests/mocks/empty.json', 'r', encoding='utf-8') as filer:
            mock_response.json.return_value = json.load(filer)
        mocker.patch.object(client, '_send', return_value=mock_response)
        client.request('GET')
        assert client._send.call_count == 1

    def test_post(self, client, mocker):
        client = BaseClient()
        client.allowed_methods = ['POST']
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        with open('tests/mocks/empty.json', 'r', encoding='utf-8') as filer:
            mock_response.json.return_value = json.load(filer)
        mocker.patch.object(client, '_send', return_value=mock_response)
        client.post({'key': 'value'})
        assert client._send.call_count == 1

    def test_put(self, client, mocker):
        client = BaseClient()
        client.allowed_methods = ['PUT']
        client.single_uri = '/test/{}'
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        with open('tests/mocks/empty.json', 'r', encoding='utf-8') as filer:
            mock_response.json.return_value = json.load(filer)
        mocker.patch.object(client, '_send', return_value=mock_response)
        client.put({'key': 'value'})
        assert client._send.call_count == 1

    def test_delete(self, client, mocker):
        client = BaseClient()
        client.allowed_methods = ['DELETE']
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        with open('tests/mocks/empty.json', 'r', encoding='utf-8') as filer:
            mock_response.json.return_value = json.load(filer)
        mocker.patch.object(client, '_send', return_value=mock_response)
        client.delete()
        assert client._send.call_count == 1

    def test_patch(self, client, mocker):
        client = BaseClient()
        client.allowed_methods = ['PATCH']
        client.single_uri = '/test/{}'
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        with open('tests/mocks/empty.json', 'r', encoding='utf-8') as filer:
            mock_response.json.return_value = json.load(filer)
        mocker.patch.object(client, '_send', return_value=mock_response)
        client.patch({'key': 'value'})
        assert client._send.call_count == 1

    def test_options(self, client, mocker):
        client = BaseClient()
        client.allowed_methods = ['OPTIONS']
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        with open('tests/mocks/empty.json', 'r', encoding='utf-8') as filer:
            mock_response.json.return_value = json.load(filer)
        mocker.patch.object(client, '_send', return_value=mock_response)
        client.options()
        assert client._send.call_count == 1


class TestAbsences:
    """Test the absences client."""

    def test_absences_list(self, client, mocker):
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        with open('tests/mocks/absences.list.json', 'r', encoding='utf-8') as filer:
            mock_response.json.return_value = json.load(filer)
        mocker.patch.object(client.absences, '_send', return_value=mock_response)
        absences = client.absences.all()
        assert len(absences) == 30
        assert client.absences._send.call_count == 1

    def test_absences_no_single_url(self, client):
        with pytest.raises(NoSingleUrl):
            client.absences.get(11)


class TestAbsencesReports:
    """
        Test the absences reports client.
        We use this class to test some methods of the base client.
    """

    def test_absences_reports_default(self, client, mocker):
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        with open('tests/mocks/absences_reports.default.json', 'r', encoding='utf-8') as filer:
            mock_response.json.return_value = json.load(filer)
        mocker.patch.object(client.absences_reports, '_send', return_value=mock_response)
        default = client.absences_reports.get_default({'resource': 1})
        assert default.relationships.get('resource', {}).get('data', {}).get('id') == '1'
        assert client.absences_reports._send.call_count == 1

    def test_absences_reports_default_404(self, client, mocker):
        """Test that the client raises an exception when the API returns a 404."""
        # sourcery skip: class-extract-method
        mock_response = mocker.Mock()
        mock_response.status_code = 404
        mocker.patch.object(client.absences_reports, '_send', return_value=mock_response)
        with pytest.raises(PageNotFoundError):
            client.absences_reports.get_default({'resource': 1})
        assert client.absences_reports._send.call_count == 1

    def test_absences_reports_default_422(self, client, mocker):
        """Test that the client raises an exception when the API returns a 422."""
        mock_response = mocker.Mock()
        mock_response.status_code = 422
        with open('tests/mocks/absences_reports.422.json', 'r', encoding='utf-8') as filer:
            mock_response.json.return_value = json.load(filer)
        mocker.patch.object(client.absences_reports, '_send', return_value=mock_response)
        with pytest.raises(BoondManagerUnprocessableEntity):
            client.absences_reports.get_default()

    def test_absences_reports_list(self, client, mocker):
        filters = {
            'endMonth': '2023-12-31',
            'startMonth': '2020-01-01',
        }
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        with open('tests/mocks/absences_reports.list.json', 'r', encoding='utf-8') as filer:
            mock_response.json.return_value = json.load(filer)
        mocker.patch.object(client.absences_reports, '_send', return_value=mock_response)
        absences_reports = client.absences_reports.all(params=filters)
        assert len(absences_reports) == 30
        assert client.absences_reports._send.call_count == 1

    def test_absences_reports_get(self, client, mocker):
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        with open('tests/mocks/absences_reports.get.24.json', 'r', encoding='utf-8') as filer:
            mock_response.json.return_value = json.load(filer)
        mocker.patch.object(client.absences_reports, '_send', return_value=mock_response)
        absences_report = client.absences_reports.get(24)
        assert absences_report.id == '24'
        assert client.absences_reports._send.call_count == 1

    def test_absences_reports_get_tab(self, client, mocker):
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        with open('tests/mocks/absences_reports.get.24.rights.json', 'r', encoding='utf-8') as filer:
            mock_response.json.return_value = json.load(filer)
        mocker.patch.object(client.absences_reports, '_send', return_value=mock_response)
        absences_report = client.absences_reports.get_tab(24, 'rights')
        assert absences_report.id == 'absencesreport_24'
        assert client.absences_reports._send.call_count == 1

    def test_absences_reports_404(self, client, mocker):
        """Test that the client raises an exception when the API returns a 404."""
        # sourcery skip: class-extract-method
        mock_response = mocker.Mock()
        mock_response.status_code = 404
        mocker.patch.object(client.absences_reports, '_send', return_value=mock_response)
        with pytest.raises(PageNotFoundError):
            client.absences_reports.get(764)
        assert client.absences_reports._send.call_count == 1

    def test_absences_reports_422(self, client, mocker):
        """Test that the client raises an exception when the API returns a 422."""
        mock_response = mocker.Mock()
        mock_response.status_code = 422
        with open('tests/mocks/absences_reports.422.json', 'r', encoding='utf-8') as filer:
            mock_response.json.return_value = json.load(filer)
        mocker.patch.object(client.absences_reports, '_send', return_value=mock_response)
        with pytest.raises(BoondManagerUnprocessableEntity):
            client.absences_reports.all()

    def test_absences_reports_403(self, client, mocker):
        """Test that the client raises an exception when the API returns a 403."""
        mock_response = mocker.Mock()
        mock_response.status_code = 403
        mocker.patch.object(client.absences_reports, '_send', return_value=mock_response)
        with pytest.raises(BoondManagerForbidden):
            client.absences_reports.all()

    def test_unknown_tab(self, client):
        with pytest.raises(UnknownTab):
            client.absences_reports.get_tab(3, 'unknown')


class TestMarketplace:
    """Test the Marketplace class."""

    def test_marketplace_default(self, client, mocker):
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        with open('tests/mocks/marketplace.default.json', 'r', encoding='utf-8') as filer:
            mock_response.json.return_value = json.load(filer)
        mocker.patch.object(client.marketplace, '_send', return_value=mock_response)
        client.marketplace.get_default()
        assert client.marketplace._send.call_count == 1

    def test_marketplace_list(self, client, mocker):
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        with open('tests/mocks/marketplace.list.json', 'r', encoding='utf-8') as filer:
            mock_response.json.return_value = json.load(filer)
        mocker.patch.object(client.marketplace, '_send', return_value=mock_response)
        marketplace = client.marketplace.all()
        assert len(marketplace) == 2
        assert client.marketplace._send.call_count == 1

    def test_marketplace_get(self, client, mocker):
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        with open('tests/mocks/marketplace.get.37934.json', 'r', encoding='utf-8') as filer:
            mock_response.json.return_value = json.load(filer)
        mocker.patch.object(client.marketplace, '_send', return_value=mock_response)
        marketplace = client.marketplace.get(100016)
        assert marketplace.id == '37934'
        assert client.marketplace._send.call_count == 1

    def test_marketplace_get_configure(self, client, mocker):
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        with open('tests/mocks/marketplace.get.37934.configure.json', 'r', encoding='utf-8') as filer:
            mock_response.json.return_value = json.load(filer)
        mocker.patch.object(client.marketplace, '_send', return_value=mock_response)
        marketplace = client.marketplace.configure('randomapptype1')
        assert marketplace.id == '37934'
        assert client.marketplace._send.call_count == 1

    def test_marketplace_put_configure(self, client, mocker):
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        with open('tests/mocks/marketplace.get.37934.configure.json', 'r', encoding='utf-8') as filer:
            mock_response.json.return_value = json.load(filer)
        mocker.patch.object(client.marketplace, '_send', return_value=mock_response)
        marketplace = client.marketplace.configure('randomapptype1',
                                                   {'data': {'attributes': {'visibility': 'allManagersAndResources'}}})
        assert marketplace.id == '37934'
        assert client.marketplace._send.call_count == 1

    def test_marketplace_refresh_token(self, client, mocker):
        mock_response = mocker.Mock()
        mock_response.status_code = 200
        jwt = get_jwt(user_token='DIjdfihdè87hdskjhd7879b', client_token='djfdfD90ndlnNoos', client_key='dskjfhdsf')
        client.marketplace.jwt_app = jwt
        with open('tests/mocks/empty.json', 'r', encoding='utf-8') as filer:
            mock_response.json.return_value = json.load(filer)
        mocker.patch.object(client.marketplace, '_send', return_value=mock_response)
        client.marketplace.refresh_token()
        assert client.marketplace._send.call_count == 1

    def test_marketplace_cant_refresh_token_without_jwt(self, client):
        with pytest.raises(ValueError):
            client.marketplace.refresh_token()
