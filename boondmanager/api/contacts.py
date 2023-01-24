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


class Contacts(DefaultEndpointMixin, BaseClient):
    """
    Search, create and manage contacts

    Tabs :

    - rights : get rights of the current user
    - information : get information
    - attached-flags : get attached flags
    - actions : get actions
    - opportunities : get opportunities
    - projects : get projects
    - purchases : get purchases
    - orders : get orders
    - invoices : get invoices
    - tasks : get tasks

    Usage :

    >>> contacts_client = Contacts()
    >>> # Get rights
    >>> contacts_client.get_tab(5, 'rights')
    >>> # Get all contacts
    >>> contacts_client.all()
    >>> # Get a contact
    >>> contacts_client.get(5)
    >>> # Create a contact
    >>> data = {...}  # See BoondManager documentation
    >>> contacts_client.post(data=data)
    >>> # Update a contact
    >>> data = {...}  # See BoondManager documentation
    >>> contacts_client.put(5, data=data)
    >>> # Delete a contact
    >>> contacts_client.delete(5)
    >>> # Get default values
    >>> contacts_client.get_default()
    """
    allowed_methods = ['GET', 'POST', 'DELETE', 'PUT']
    list_uri = '/contacts'
    single_uri = '/contacts/{}'
    tabs = ['rights', 'information', 'attached-flags', 'actions', 'opportunities', 'projects', 'purchases', 'orders',
            'invoices', 'tasks']
