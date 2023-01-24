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


class Contracts(DefaultEndpointMixin, BaseClient):
    """Create, search and manage contracts

    Tabs :

    - advantages : get advantages
    - rights : get rights of the current user
    - download : Manage contract's formatted file
    - tasks : get tasks

    Usage :

    >>> contracts_client = Contracts()
    >>> # Get rights
    >>> contracts_client.get_tab(5, 'rights')
    >>> # Get all contracts
    >>> contracts_client.all()
    >>> # Get a contract
    >>> contracts_client.get(5)
    >>> # Create a contract
    >>> data = {...}  # See BoondManager documentation
    >>> contracts_client.post(data=data)
    >>> # Update a contract
    >>> data = {...}  # See BoondManager documentation
    >>> contracts_client.put(5, data=data)
    >>> # Delete a contract
    >>> contracts_client.delete(5)
    >>> # Get default values
    >>> contracts_client.get_default()
    """
    allowed_methods = ['GET', 'POST', 'DELETE', 'PUT']
    list_uri = '/contracts'
    single_uri = '/contracts/{}'
    tabs = ['advantages', 'rights', 'download', 'tasks']


class BoondmanagerContracts(BaseClient):
    """Manage boondmanager contracts

    Usage :

    >>> boondmanager_contracts_client = BoondmanagerContracts()
    >>> # Get a contract
    >>> boondmanager_contracts_client.get(5)
    >>> # Update a contract
    >>> data = {...}  # See BoondManager documentation
    >>> boondmanager_contracts_client.put(5, data=data)"""
    allowed_methods = ['GET', 'PUT']
    single_uri = '/boondmanager-contracts/{}'
