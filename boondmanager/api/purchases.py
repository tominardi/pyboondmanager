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


class Purchases(DefaultEndpointMixin, BaseClient):
    """Search, create and manage purchases

    Tabs :

    - rights : get rights of the current user
    - informations : get informations
    - attached-flags : get attached flags
    - simulation : get simulation
    - payments : get payments
    - download : get download
    - tasks : get tasks

    Usage :

    >>> purchases_client = Purchases()
    >>> # Get rights
    >>> purchases_client.get_tab(5, 'rights')
    >>> # Get all purchases
    >>> purchases_client.all()
    >>> # Get a purchase
    >>> purchases_client.get(5)
    >>> # Create a purchase
    >>> data = {...}  # See BoondManager documentation
    >>> purchases_client.post(data=data)
    >>> # Update a purchase
    >>> data = {...}  # See BoondManager documentation
    >>> purchases_client.put(5, data=data)
    >>> # Delete a purchase
    >>> purchases_client.delete(5)
    >>> # Get default values
    >>> purchases_client.get_default()
    """
    allowed_methods = ['GET', 'POST', 'DELETE', 'PUT']
    list_uri = '/purchases'
    single_uri = '/purchases/{}'
    tabs = ['rights', 'informations', 'attached-flags', 'simulation', 'payments', 'download', 'tasks']
