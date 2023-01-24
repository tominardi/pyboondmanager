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


class Orders(DefaultEndpointMixin, BaseClient):
    """Search, create and manage orders

    Tabs :

    - rights : get rights of the current user
    - information : get information
    - attached-flags : get attached flags
    - invoices : get invoices
    - download : get download
    - actions : get actions
    - tasks : get tasks

    Usage :

    >>> orders_client = Orders()
    >>> # Get rights
    >>> orders_client.get_tab(5, 'rights')
    >>> # Get all orders
    >>> orders_client.all()
    >>> # Get an order
    >>> orders_client.get(5)
    >>> # Create an order
    >>> data = {...}  # See BoondManager documentation
    >>> orders_client.post(data=data)
    >>> # Update an order
    >>> data = {...}  # See BoondManager documentation
    >>> orders_client.put(5, data=data)
    >>> # Delete an order
    >>> orders_client.delete(5)
    >>> # Get default values
    >>> orders_client.get_default()
    """
    allowed_methods = ['GET', 'POST', 'DELETE', 'PUT']
    list_uri = '/orders'
    single_uri = '/orders/{}'
    tabs = ['rights', 'information', 'attached-flags', 'invoices', 'download', 'actions', 'tasks']
