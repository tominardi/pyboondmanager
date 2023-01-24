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
from .base import BaseClient


class Deliveries(BaseClient):
    """Seach, create and manage deliveries

    Tabs :

    - rights : get rights of the current user
    - advantages : get advantages
    - delivery-order-download : get delivery order download
    - download : get download
    - send : get send
    - renew : get renew
    - tasks : get tasks

    Usage :

    >>> deliveries_client = Deliveries()
    >>> # Get rights
    >>> deliveries_client.get_tab(5, 'rights')
    >>> # Get all deliveries
    >>> deliveries_client.all()
    >>> # Get a delivery
    >>> deliveries_client.get(5)
    >>> # Create a delivery
    >>> data = {...}  # See BoondManager documentation
    >>> deliveries_client.post(data=data)
    >>> # Update a delivery
    >>> data = {...}  # See BoondManager documentation
    >>> deliveries_client.put(5, data=data)
    """
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']
    list_uri = '/deliveries'
    single_uri = '/deliveries/{}'
    tabs = ['rights', 'advantages', 'delivery-order-download', 'download', 'send', 'renew', 'tasks']


class DeliveriesGroupments(BaseClient):
    """Seach, create and manage deliveries groupments

    Usage :

    >>> deliveries_groupments_client = DeliveriesGroupments()
    >>> # Get all deliveries groupments
    >>> deliveries_groupments_client.all()
    """
    allowed_methods = ['GET']
    list_uri = '/deliveries-groupments'
