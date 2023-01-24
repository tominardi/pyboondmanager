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


class Payments(DefaultEndpointMixin, BaseClient):
    """Search, create and manage payments

    Tabs :

    - rights : get rights of the current user
    - tasks : get tasks

    Usage :

    >>> payments_client = Payments()
    >>> # Get rights
    >>> payments_client.get_tab(5, 'rights')
    >>> # Get all payments
    >>> payments_client.all()
    >>> # Get a payment
    >>> payments_client.get(5)
    >>> # Create a payment
    >>> data = {...}  # See BoondManager documentation
    >>> payments_client.post(data=data)
    >>> # Update a payment
    >>> data = {...}  # See BoondManager documentation
    >>> payments_client.put(5, data=data)
    >>> # Delete a payment
    >>> payments_client.delete(5)
    >>> # Get default values
    >>> payments_client.get_default()
    """
    allowed_methods = ['GET', 'POST', 'DELETE', 'PUT']
    list_uri = '/payments'
    single_uri = '/payments/{}'
    tabs = ['rights', 'tasks']
