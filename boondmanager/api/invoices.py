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


class Invoices(DefaultEndpointMixin, BaseClient):
    """Seach, create and manage invoices

    Tabs :

    - rights : get rights of the current user
    - information : get information
    - attached-flags : get attached flags
    - actions : get actions
    - download : get download
    - send : get send
    - tasks : get tasks

    Usage :

    >>> invoices_client = Invoices()
    >>> # Get rights
    >>> invoices_client.get_tab(5, 'rights')
    >>> # Get all invoices
    >>> invoices_client.all()
    >>> # Get an invoice
    >>> invoices_client.get(5)
    >>> # Create an invoice
    >>> data = {...}  # See BoondManager documentation
    >>> invoices_client.post(data=data)
    >>> # Update an invoice
    >>> data = {...}  # See BoondManager documentation
    >>> invoices_client.put(5, data=data)
    >>> # Delete an invoice
    >>> invoices_client.delete(5)
    >>> # Get default values
    >>> invoices_client.get_default()
    """
    allowed_methods = ['GET', 'POST', 'DELETE', 'PUT']
    single_uri = '/invoices'
    list_uri = '/invoices/{}'
    tabs = ['rights', 'information', 'attached-flags', 'actions', 'download', 'send', 'tasks']
