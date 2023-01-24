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


class Accounts(DefaultEndpointMixin, BaseClient):
    """Search, create and manage accounts

    Tabs :

    - connect : connect to the account

    Usage :

    >>> accounts_client = Accounts()
    >>> # Get all accounts
    >>> accounts_client.all()
    >>> # Get an account
    >>> accounts_client.get(5)
    >>> # Connect to the account
    >>> accounts_client.post_tab(5, 'connect')
    >>> # Create an account
    >>> data = {...}  # See BoondManager documentation
    >>> accounts_client.post(data=data)
    >>> # Update an account
    >>> data = {...}  # See BoondManager documentation
    >>> accounts_client.put(5, data=data)
    >>> # Get default values
    >>> accounts_client.get_default()
    """
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']
    list_uri = '/accounts'
    single_uri = '/accounts/{}'
    tabs = ['connect']
