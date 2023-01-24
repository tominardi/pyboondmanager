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
from .base import BaseClient, DefaultEndpointMixin


class Marketplace(DefaultEndpointMixin, BaseClient):
    """Search, create and manage apps

    Tabs :

    - rights : Get rights for current user
    - install : Install an app
    - validate : Validate an app
    - configure : Configure an app
    - uninstall : Uninstall an app
    - logo : Manage logo
    - publish : Publish an app

    Usage :

    >>> marketplace_client = Marketplace()
    >>> # Get rights
    >>> marketplace_client.get_tab(5, 'rights')
    >>> # Get all apps
    >>> marketplace_client.all()
    >>> # Get an app
    >>> marketplace_client.get(5)
    >>> # Create an app
    >>> data = {...}  # See BoondManager documentation
    >>> marketplace_client.post(data=data)
    >>> # Update an app
    >>> data = {...}  # See BoondManager documentation
    >>> marketplace_client.put(5, data=data)
    >>> # Delete an app
    >>> marketplace_client.delete(5)
    >>> # Install an app
    >>> marketplace_client.post_tab(5, 'install')
    >>> # Validate an app
    >>> marketplace_client.post_tab(5, 'validate')
    >>> # Configure an app
    >>> marketplace_client.configure(5)
    >>> # Uninstall an app
    >>> marketplace_client.post_tab(5, 'uninstall')
    >>> # Get default values
    >>> marketplace_client.get_default()
    >>> # Configure an app
    >>> data = {...}  # See BoondManager documentation
    >>> marketplace_client.configure('app_code', data=data)
    >>> # Refresh the app token
    >>> marketplace_client.refresh_token()
    """
    allowed_methods = ['GET', 'POST', 'DELETE', 'PUT']
    list_uri = '/marketplace'
    single_uri = '/marketplace/{}'
    tabs = ['rights', 'install', 'validate', 'configure', 'uninstall', 'logo', 'publish']

    def configure(self, app_code, data=None):
        if data:
            return self.request('PUT', forced_uri=f'{self.list_uri}/{app_code}/configure', post_data=data)
        return self.request('GET', forced_uri=f'{self.list_uri}/{app_code}/configure')

    def refresh_token(self):
        """
        Refresh the app token.

        Warning: this method is only available with the jwt app auth
        """
        if not self.jwt_app:
            raise ValueError('This method is only available with the jwt app auth')
        return self.request('POST', forced_uri=f'{self.list_uri}/refresh-token')
